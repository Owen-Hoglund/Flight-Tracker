import mysql.connector
import flightGroupClassMk2
import groupHandlerClass
from datetime import datetime

# Opens the connection to our database
# ----------------------------------------------------------------------------------------------------------------------------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="payload.snowdrop.vacancy",
    database="testingenvironmentdatabase"
)
cursor = db.cursor(buffered=True)
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# TODO: Need to find a better place for this, something this basic should not be here it should be in a library of useful things
# Converts the string date into datetime
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def strToDateTime(exampleDate):
    return datetime.strptime(exampleDate, "%Y-%m-%d")
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# This will recreate the main parent table if there is a catastrophic failure or if I wipe all the data to start fresh


def createAlphaTable():
    sqlstring = "CREATE TABLE flightgroups (email VARCHAR(50) NOT NULL, date_lower_bound datetime NOT NULL, date_upper_bound datetime NOT NULL, destination VARCHAR(3) NOT NULL, stayRangeLow int NOT NULL, stayRangeHigh int NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"
    cursor.execute(sqlstring)


# Takes in an instance of the group handler, then iterates over the groups contained within it
# for each group adding a new row to the flightgroups table in SQL, then creates a "unique" table associated with each group
# Named after the group email address, this table contains the airport-passengercount list associated with each group
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def groupTabler(handle):
    # Iterates over groups in handler
    for group in handle.groups:
        # converts time string to datetime
        low = strToDateTime(group.dateLowerBound)
        high = strToDateTime(group.dateUpperBound)

        # inserts new group data row to the flightgroups table
        cursor.execute("INSERT INTO flightgroups VALUES (%s,%s,%s,%s,%s,%s, NULL)", (
            group.email, low, high, group.destination, group.stayRange[0], group.stayRange[1]))
        # Creates new table for the airport-passenger list
        cursor.execute("CREATE TABLE %s (outbound_airport VARCHAR(50), passenger_count int)" %
                       group.email.removesuffix('@gmail.com'))

        # iterates over the current groups originList
        for i in group.groupOrigins:
            # Inserts each airport-passenger tuple to the newly created table
            sqlstring = "INSERT INTO " + group.email.removesuffix(
                '@gmail.com') + " VALUES ('" + str(i[0]) + "'," + str(int(i[1])) + ")"
            cursor.execute(sqlstring)
    # finalizes all of the above changes to the database
    db.commit()

    # Selects every row from the flightgroups table, we are preparing to refresh the pickle jar
    cursor.execute("SELECT * FROM flightgroups")
    count = 1

    # Creating a new handle instance to load flight groups into from the flightgroups table
    newhandle = groupHandlerClass.handler()

    # Now we are iterating over rows, preparing to extract data from the row
    for i in cursor:
        # Now we create a blank variable, a list which we will use to pass create a new flightGroup from
        flightGroupArguments = []
        for j in i:
            flightGroupArguments.append(j)
        cursor2 = db.cursor(buffered=True)
        temptablename = str(i[0].removesuffix('@gmail.com'))
        tempstring = "SELECT * FROM " + temptablename
        cursor2.execute(tempstring)
        tempOriginsList = []
        for k in cursor2:
            tempOriginsList.append(k)
        tempflightgroup = flightGroupClassMk2.flightGroup(
            flightGroupArguments[3], flightGroupArguments[1],
            flightGroupArguments[2], (flightGroupArguments[4],
                                      flightGroupArguments[5]), flightGroupArguments[0] + "@gmail.com",
            tempOriginsList)
        newhandle.groups.append(tempflightgroup)
        newhandle.save()

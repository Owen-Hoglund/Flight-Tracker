from re import S
import mysql.connector
import flightGroupClassMk2
import groupHandlerClass
from datetime import datetime, date, timedelta
import flightProjectHelper as utility

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

# These will recreate the main parent tables if there is a catastrophic failure or if I wipe all the data to start fresh
# otherwise run these from a separate file to begin a new database for testing on another machine
# ----------------------------------------------------------------------------------------------------------------------------------------------------
 
def createAlphaTable():  # CREATES flightgroup table
    sqlstring = "CREATE TABLE flightgroups (email VARCHAR(50) NOT NULL, date_lower_bound datetime NOT NULL, date_upper_bound datetime NOT NULL, destination VARCHAR(3) NOT NULL, stayRangeLow int NOT NULL, stayRangeHigh int NOT NULL, PRIMARY KEY(email))"
    cursor.execute(sqlstring)
    
def createBetaTable():  # Creates flight_group_airport_list table
    sqlstring = "CREATE TABLE flight_group_airport_list (email VARCHAR(50) NOT NULL, origin_airport VARCHAR(3) NOT NULL, passenger_count int NOT NULL, FOREIGN KEY(email) REFERENCES flightgroups(email))"
    cursor.execute(sqlstring)
    
def createGammaTable(): # Creates flight_group_daily_price table
    sqlstring = "CREATE TABLE flight_group_daily_price (email VARCHAR(50) NOT NULL, date VARCHAR(50) NOT NULL, price_departure int, price_return int, FOREIGN KEY(email) REFERENCES flightgroups(email)))"
    cursor.execute(sqlstring)
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# The following block of code pushes all the data from a list of flightgroup objects (a 'handle') into the database
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def groupTabler(handle):
    
    # Iterates over groups in handler
    for group in handle.groups:
        # converts time string to datetime
        low = utility.str_to_date_time(group.dateLowerBound)
        high = utility.str_to_date_time(group.dateUpperBound)

        # inserts new group data row to the flightgroups table
        cursor.execute("INSERT INTO flightgroups VALUES (%s,%s,%s,%s,%s,%s)", (
            group.email, low, high, group.destination, group.stayRange[0], group.stayRange[1]))
        
        # iterates over the current groups originList
        for i in group.groupOrigins:
            # Inserts each airport-passenger tuple to the flight_group_airport_list
            sqlstring = "INSERT INTO flight_group_airport_list (email, origin_airport, passenger_count) VALUES ('" + group.email + "', '" + str(i[0]) + "', " + str(int(i[1])) + ")"
            cursor.execute(sqlstring)
            
        # Add dates into the flight_group_daily_price table for the current group
        for day in utility.daterange(low, high):
            sqlstring = "INSERT INTO flight_group_daily_price (email, date, price_departure, price_return) VALUES ('" + group.email + "', '" + utility.date_time_to_str(day) + "', 0, 0)"
            # print('\n' + sqlstring + '\n')
            cursor.execute(sqlstring)
        
    # finalizes all of the above changes to the database. Conveniently 
    # if any errors occur in the above code none of these changes are
    # committed and you are left with a clean database still
    db.commit()
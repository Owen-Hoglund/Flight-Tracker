from nntplib import GroupInfo
from re import S
from tkinter.tix import DisplayStyle
from tokenize import group
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

# This initializes the necessary tables
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def initalize_tables():
    # CREATES flightgroup table
    sqlstring = "CREATE TABLE if not exists flightgroups (email VARCHAR(50) NOT NULL, date_lower_bound datetime NOT NULL, date_upper_bound datetime NOT NULL, destination VARCHAR(3) NOT NULL, stayRangeLow int NOT NULL, stayRangeHigh int NOT NULL, PRIMARY KEY(email))"
    cursor.execute(sqlstring)
    
    # Creates flight_group_airport_list table
    sqlstring = "CREATE TABLE if not exists flight_group_airport_list (email VARCHAR(50) NOT NULL, origin_airport VARCHAR(3) NOT NULL, passenger_count int NOT NULL, FOREIGN KEY(email) REFERENCES flightgroups(email))"
    cursor.execute(sqlstring)
    
    # Creates flight_group_daily_price table
    sqlstring = "CREATE TABLE if not exists flight_group_daily_price (email VARCHAR(50) NOT NULL, date VARCHAR(50) NOT NULL, price_departure int, price_return int, FOREIGN KEY(email) REFERENCES flightgroups(email))"
    cursor.execute(sqlstring)
    
    # Creates iata_date_price table
    sqlstring = "CREATE TABLE if not exists iata_date_price (iata VARCHAR(50), date VARCHAR(50), price_departure int, price_return int, PRIMARY KEY (iata, date))"
    cursor.execute(sqlstring)
    sqlstring = "ALTER TABLE iata_iata_date_price CHANGE COLUMN `iata VARCHAR(50) NOT NULL, CHANGE COLUMN `date` `date` VARCHAR(50) NOT NULL ,ADD PRIMARY KEY (`iata, `date`)"
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
            cursor.execute(sqlstring)
        
        # Add dates into the iata_date_price table for the current group
        for day in utility.daterange(low, high):
            for origins in group.groupOrigins:
                destination = group.destination
                itinerary_pair = utility.iata_pair(destination, origins[0])
                sqlstring = "INSERT IGNORE INTO iata_date_price (iata, date, price_departure, price_return) VALUES ('" + itinerary_pair + "', '" + utility.date_time_to_str(day) + "', 0, 0)"
                cursor.execute(sqlstring)
            
    # finalizes all of the above changes to the database. Conveniently 
    # if any errors occur in the above code none of these changes are
    # committed and you are left with a clean database still
    db.commit()
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    # The following block of code will run through the database and populate a handle (group handler class) with the data associated with each group
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
def load(handle):
    # First we select all rows from the flightgroups table 
    cursor.execute("SELECT * FROM flightgroups")
    
    # Now we load these rows into a list of rows 
    flightgroups_database = cursor.fetchall()
    
    # Now, for each row, we extract the data to reform a group, this requires accessing another table, the flight_group_airport_list
    for row in flightgroups_database:
        # We select the aforementioned table
        cursor.execute("SELECT * FROM flight_group_airport_list WHERE email = '" + row[0] + "'")
        
        # Fetch the rows that we need
        group_airport_list = cursor.fetchall()
        
        # Create a new blank list of airport-passengers tuples to load into our flightgroup 
        airport_list = []
        
        # Append each airport-passenger tuple to the list
        for item in group_airport_list:
            airport_list.append(item[1:])
        
        # Finally we create a new flightgroup instance with the data extracted from the tables
        newGroup = flightGroupClassMk2.flightGroup(row[3], row[1], row[2], (row[4], row[5]), row[0], airport_list)
        
        # And add it to the group handler 
        handle.newGroup(newGroup)
        # ----------------------------------------------------------------------------------------------------------------------------------------------------
        
def populate_price_random_generator(handler):
    cursor.execute("SELECT * FROM iata_date_price WHERE price_return = 0 AND price_departure = 0")
    airport_to_airport_price = cursor.fetchall()
    for itinerary in airport_to_airport_price:
        itinerary_date = itinerary[1]
        cursor.execute("UPDATE iata_date_price SET price_departure=%s WHERE iata = %s AND date=%s", (utility.random_price_generator(), itinerary[0], itinerary_date))
        cursor.execute("UPDATE iata_date_price SET price_return=%s WHERE iata = %s AND date=%s", (utility.random_price_generator(), itinerary[0], itinerary_date))
    db.commit()
    
def populate_daily_price():
    print("Starting")
    sqlstring = "SELECT * FROM flightgroups"
    cursor.execute(sqlstring)
    groups = cursor.fetchall()
    
    # We Populate prices by group first
    for group in groups:
        # for simplicity, we will save all the static variables from each group below
        email = group[0]
        dateLow = group[1]
        dateHigh = group[2]
        destination = group[3]
        origins_tuples = []
        # Now we store the current groups origin list tuples. origin[1] is iata code origin[2] is the number of passengers traveling 
        cursor.execute("SELECT * FROM flight_group_airport_list WHERE email = '" + group[0] + "'" )
        origin_list = cursor.fetchall()
        # Now we need to iterate over the days of travel. We do this using the generator in the flightProjectHelper
        for day in utility.daterange(dateLow, dateHigh):
            # The crux comes now. We need to sum the cost to fly from A -> B and B -> A separately and then put them into the flight_group_daily_price table
            # The daily itinerary prices are stored in the iata_date_price table.
            # We do this by iterating over the itineraries that we have saved in the origin_list
            cost_to_depart = 0
            cost_to_return = 0
            for origin in origin_list:
                itinerary = utility.iata_pair(destination, origin[1])
                sqlstring = "SELECT * FROM iata_date_price WHERE iata = '%s' and date='%s'" % (itinerary, utility.date_time_to_str(day))
                cursor.execute(sqlstring)
                costs_for_day = cursor.fetchall()
                for costs in costs_for_day:
                    # Basic idea is that if Destination is NOT the first iata code in the pair, then price_departure == price_departure
                    # if Destination is the first iata code in the pair, then the true price of departure is price_return
                    if(utility.departure_or_return(destination, itinerary) == 'departure'):
                        # Add departure_price to cost to depart
                        cost_to_depart += costs[2] * origin[2]
                        cost_to_return += costs[3] * origin[2]
                    if(utility.departure_or_return(destination, itinerary) == 'return'):
                        # Add departure_price to cost to depart
                        cost_to_depart += costs[3] * origin[2]
                        cost_to_return += costs[2] * origin[2]
                    #print("itinerary: " + costs[0] + " DATE: " + costs[1] + "   Cost To depart: " + str(costs[2]) + "    Cost to return: " + str(costs[3]))
            # Add price to depart and return to flight_group_daily_price
            sqlstring = "UPDATE flight_group_daily_price SET price_departure=%s WHERE email = '%s' AND date='%s'" % (cost_to_depart, email, utility.date_time_to_str(day))
            cursor.execute(sqlstring)
            sqlstring = "UPDATE flight_group_daily_price SET price_return=%s WHERE email = '%s' AND date='%s'" % (cost_to_return, email, utility.date_time_to_str(day))
            cursor.execute(sqlstring)
    db.commit()


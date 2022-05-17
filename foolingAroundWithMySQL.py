import mysql.connector
import flightGroupClassMk2
from datetime import datetime



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="payload.snowdrop.vacancy",
    database="testingenvironmentdatabase"
)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE flightGroups (email VARCHAR(50) NOT NULL, dateLowerBound datetime NOT NULL, dateUpperBound datetime NOT NULL, destination VARCHAR(50) NOT NULL, stayRangeLow int NOT NULL, stayRangeHigh int NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

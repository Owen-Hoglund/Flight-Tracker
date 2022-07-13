from cgitb import handler
from email import generator
from msilib.schema import File
from tkinter import GROOVE
import mysqlx

from pure_eval import group_expressions
import groupHandlerClass
import flightGroupClassMk2
import exampleGroupGenerator
import dataBaseManager

# This will populate random groups on initialization of the database
def populate_groups():
    handler = groupHandlerClass.handler()
    for i in range(1):
        newGroup = flightGroupClassMk2.flightGroup
        newGroup = exampleGroupGenerator.random_group_maker()
        handler.newGroup(newGroup)
    dataBaseManager.groupTabler(handler)
    del handler

# In the future, this is where you will connect to a flight price API to populate individual prices for 
# all itineraries in the group
def populate_prices_from_API():
    pass

# For proof of concept, this generates completely random prices for flights.
def populate_price_random_generator():
    handler = groupHandlerClass.handler()
    dataBaseManager.load(handler)
    dataBaseManager.populate_price_random_generator(handler)
    del handler



first_time = input("Is this your first time runnning this software? (y/n) ")
print(first_time)
while not ((first_time != 'y') or (first_time != 'n')):
    first_time = input("Invalid Entry. Is this your first time runnning this software? (y/n) ")
if first_time == 'y':
    dataBaseManager.initalize_tables()
    
populate = input("Would you like to populate the tables with randomized entries? (y/n) ")
while not ((populate != 'y') or (populate != 'n')):
    populate = input("Invalid Entry. Would you like to populate the tables with 10 randomized entries? (y/n) ")
if populate == 'y':
    populate_groups()
    

API_active = input("Do you have a running API to populate prices? (y/n)")
while not ((API_active != 'y') or (API_active != 'n')):
    API_active = input("Invalid Entry. Would you like to populate the tables with 10 randomized entries? (y/n) ")
if API_active == 'y':
    populate_prices_from_API()
else:
    price = input("Would you like to populate the price table with randomized prices? (y/n) ")
    while not ((price != 'y') or (price != 'n')):
        price = input("Invalid Entry. Would you like to populate the price table with randomized prices? (y/n) ")
    if price == 'y':
        populate_price_random_generator()
        
# populatePrice = input("Would you like to populate the daily prices from given daily itinerary prices? (y/n) ")
# while not ((populatePrice != 'y') or (populatePrice != 'n')):
#     populatePrice = input("Invalid Entry. Would you like to populate the tables with 10 randomized entries? (y/n) ")
# if populate == 'y':
#     print("working")
dataBaseManager.populate_daily_price()
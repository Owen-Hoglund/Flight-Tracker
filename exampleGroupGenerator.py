from flightGroupClassMk2 import flightGroup
import random
from datetime import date, timedelta
import string

# Creates a randomized flight group
#----------------------------------------------------------------------------------------------------------------------
def random_group_maker():
    orig_dest = origin_destination()
    temp_stayRange = random.randint(1, 30)
    temp_departure = random_date_generator()
    temp_return = date_finder(temp_departure , temp_stayRange)
    date_format = time_formatter(temp_departure, temp_return)
    email = email_generator()

    return flightGroup(orig_dest[0], date_format[0], date_format[1], temp_stayRange, email, orig_dest[1])
#----------------------------------------------------------------------------------------------------------------------



# Generates a random date 
#----------------------------------------------------------------------------------------------------------------------
def random_date_generator():
    x = random.randint(1, 365)
    return date.today() + timedelta(days= x)
#----------------------------------------------------------------------------------------------------------------------



# Generates a date n days after a given date, where n is the length of stay of the trip
#----------------------------------------------------------------------------------------------------------------------
def date_finder(departDate, stayRange):
    return departDate + timedelta(days = stayRange)
#----------------------------------------------------------------------------------------------------------------------



# This function generates the groupOrigins and destination Attributes
#----------------------------------------------------------------------------------------------------------------------
def origin_destination():
    # Expandable with however many iata codes youd like, but this should be sufficient for testing purposes

    airport_list = ['MSP', 'YYZ','BOS','AHE','GIG','IXR','LED','NIO','HRM','MSY','PVG','SYD','MAD','CDG']

    loop_range = len(airport_list)
    temp = []
    # Loop builds list of (airport, passengers)
    for i in range(random.randint(1,loop_range - 1)):
        # x chooses a random index from the airport list, y chooses a random number of passengers
        x = random.randint(0, len(airport_list) - 1)
        y = random.randint(1,10)
        
        # Add random airport-passenger count to list
        temp.append((airport_list[x], y))

        # We then remove the airport from our list of potential airports
        airport_list.remove(airport_list[x])
    
    # This sets the destination from the remainder of the airports 
    temp_destination = airport_list[random.randint(0, len(airport_list) - 1)]
    return [temp_destination, temp]
#----------------------------------------------------------------------------------------------------------------------



# Takes two dates and returns them as a tupple of strings in the format YYYY-MM-DD
#----------------------------------------------------------------------------------------------------------------------
def time_formatter(depart, returndate):
    d = depart.strftime("%Y") + "-" + depart.strftime("%m") + "-" + depart.strftime("%d")
    r = returndate.strftime("%Y") + "-" + returndate.strftime("%m") + "-" + returndate.strftime("%d")
    return [d,r]
#----------------------------------------------------------------------------------------------------------------------

# Generates a random email
#----------------------------------------------------------------------------------------------------------------------
def email_generator():
    temp_email = ''
    x = random.randint(4, 12)
    for i in range(x):
        temp_email += random.choice(string.ascii_letters)
    temp_email += '@gmail.com'
    return temp_email

#----------------------------------------------------------------------------------------------------------------------
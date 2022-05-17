from flightGroupClassMk2 import flightGroup
import random
from datetime import date, timedelta
import string

# Creates a randomized flight group
#----------------------------------------------------------------------------------------------------------------------
def random_group_maker():
    orig_dest = origin_destination()
    temp_stayRange = range_generator()
    temp_dateLowerBound = random_date_generator()
    temp_dateUpperBound = date_finder(temp_dateLowerBound , temp_stayRange)
    date_format = time_formatter(temp_dateLowerBound, temp_dateUpperBound)
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
# limited by 30 days for now, for easier data crunching, but not restricted by the class itsself
#----------------------------------------------------------------------------------------------------------------------
def date_finder(dateLowerBound, stayRange):
    return dateLowerBound + timedelta(days = stayRange[1] + random.randint(1, 30))
#----------------------------------------------------------------------------------------------------------------------



# This function generates the groupOrigins and destination Attributes
#----------------------------------------------------------------------------------------------------------------------
def origin_destination():
    # Expandable with however many iata codes youd like, but this should be sufficient for testing purposes

    airport_list = ['MSP', 'YYZ','BOS','LON','GIG','IXR','LED','NIO','HRM','MSY','PVG','SYD','MAD','CDG']

    loop_range = len(airport_list)
    temp = []
    # Loop builds list of (airport, passengers)
    for i in range(random.randint(2,loop_range - 1)):
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
def time_formatter(dateLowerBound, dateUpperBound):
    d = dateLowerBound.strftime("%Y") + "-" + dateLowerBound.strftime("%m") + "-" + dateLowerBound.strftime("%d")
    r = dateUpperBound.strftime("%Y") + "-" + dateUpperBound.strftime("%m") + "-" + dateUpperBound.strftime("%d")
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



# Generates a tuple of integers (x, y) that represent the range of stay length the group is interested in (e.g 5-10 days)
#----------------------------------------------------------------------------------------------------------------------
def range_generator():
    x = random.randint(1, 30)
    y = random.randint(1, 30)
    return (min(x, y), max(x, y))
    
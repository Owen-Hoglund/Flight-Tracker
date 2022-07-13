from datetime import date, timedelta, datetime
import random

# Takes a DATETIME object and returns it in YYYY-mm-dd
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def date_time_to_str(date):
    return date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Takes a String date and returns it as a DATETIME OBJECT
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def str_to_date_time(date):
    return datetime.strptime(date, "%Y-%m-%d")
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# This is a generator used for iteration over spans of time ( ie "for day in daterange(start_date, end_date): ")
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# Self Explanatory
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def random_date_generator():
    x = random.randint(1, 365)
    return date.today() + timedelta(days= x)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Random Price Generator
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def random_price_generator():
    return random.randint(100, 1000)
# ----------------------------------------------------------------------------------------------------------------------------------------------------



def iata_pair(iata1, iata2):
    # Organize by Alpha
    # Concatenate AAA-BBB
    iata_list = [iata1, iata2]
    iata_list.sort()
    return iata_list[0] + "-" + iata_list[1]

def departure_or_return(destination, iata_pair):
    first = iata_pair[0:3]
    if destination == first:
        return "return"
    else:
        return "departure"

# INSERT RANDOM FLIGHT PRICE DATA FOR TESTING PURPOSES

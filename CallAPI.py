import pandas as pd
from amadeus import Client, ResponseError
import sqlite3


#sets airport codes 
origin_airport = 'MAD'
destination_airport =  'ATH'

a = g.group()
a.create()


conn = sqlite3.connect('groupflights.db')
c = conn.cursor()


#authenticates API requests
amadeus = Client(
    client_id='',
    client_secret=''
)

#makes API request using amadeus' library (I think it is some kind of blend with the requests library because syntax at end of methods seems similar)
try:
    response = amadeus.shopping.flight_offers_search.get( #this is a method they have written themselves to access the flight offers search API endpoint (perhaps language here isnt correct but you get the idea)
        originLocationCode= origin_airport, # self explanatory
        destinationLocationCode=destination_airport, # self explanatory
        departureDate='2022-11-01', # self explanatory also I should go back later and turn this into a variable
        adults=1 # self explanatory 
        )

    df = pd.DataFrame(response.data) # converts the API response, which returns a python list into a dataframe. 
    df.to_csv('raw_flight_data.csv', index=False) # converts the dataframe into a csv file for easier manipulation. 

except ResponseError as error:
    print(error)




print(response.data[0])
print(type(response.data[0]))


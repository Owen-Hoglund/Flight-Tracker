import requests
import json
import time
import threading
import pandas as pd
from amadeus import Client, ResponseError

#sets airport codes 
origin_airport = 'BOS'
destination_airport =  'MSP'

#authenticates API requests

amadeus = Client(
    client_id='EwzXZuAVbWHGL4s3u1uQaHAsmOkaOOSA',
    client_secret='xDIAHTjR2hy8dK53'
)

#makes API request using amadeus' library (I think it is some kind of blend with the requests library because syntax at end of methods seems similar)
try:
    response = amadeus.shopping.flight_offers_search.get( #this is a method they have written themselves to access the flight offers search API endpoint (perhaps language here isnt correct but you get the idea)
        originLocationCode= 'MAD', # self explanatory
        destinationLocationCode='LON', # self explanatory
        departureDate='2022-10-05', # self explanatory also I should go back later and turn this into a variable
        adults=1 # self explanatory 
        )

    # I think I should be able to manipulate the above API call quite a lot actually. I should be able to set return dates/lengths of stays/ranges of stays. 
    # Probably should do this before proceeding with data manip as the response is likely to look a lot different when I get it to to the actual call I want.

    #probably it is possible/easier/faster to skip the following two lines of code and convert straight from python list to a csv file
    # or actually XML because I ultimately want to fuck with this table using SQL

    print(type(response.data))
    while 2 > 1:
        x = int(input("Enter first index: "))
        y = int(input("Enter second index: "))
        print(response.data[x][y])
        print("\n")

    df = pd.DataFrame(response.data) # converts the API response, which returns a python list into a dataframe. 
    df.to_csv('raw_flight_data.csv', index=False) # converts the dataframe into a csv file for easier manipulation. 

except ResponseError as error:
    print(error)
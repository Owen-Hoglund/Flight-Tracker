import sqlite3
import os.path
import csv
import pickle

# The following code will contains the flightgroup class. This class is the fundamental building block for the entire project
# In it is stored every piece of vital information for the project to run:
# It also contains methods which will allow one to manipulate, save, view, the data associated with the class instance
#
class FlightGroup:

    def __init__(self, destination, origins, departDate, returnDate, stayRange, key): # initializes the class instance via from_input and from_file 
        self.destination = destination
        self.origins = origins
        self.departDate = departDate
        self.returnDate = returnDate 
        self.stayRange = stayRange
        self.key = key

    @classmethod
    def from_input(cls): #from_input populates an instance of a flightgroup from user input
        temp = []
        temp1 = " "
        temp2 = 0
        # Following loop allows the user to continue adding more and more people to the group
        while input("Add travelers in this Group? y/n: ") != 'n': # this loop is the piece that allows the user to input multiple airports as origins
            temp1 = input("Enter departing Airport Code:  ")
            temp2 = input("How many travelers will be departing from this airport:  ")
            temp.append([temp1, temp2])
        #Returns the necessary arguments to instantiate the class instance
        return cls(
            input("Enter destination Airport Code:  "),
            temp,
            input("Enter the Date you would like to depart:   "),
            input("Enter the Date you would like to return:   "),
            input("How many days would you like to stay:    ")
        )
    
    @classmethod
    def from_file(cls): # from_file populates an instance of a flight group from a serialized file 
        with open('flightGroupData.pkl', 'rb') as FGhandler:
            return pickle.load(FGhandler)

    def save(self): # This function pickles the current group for future use
        #opens the file and prepares to write to it. 'wb' --> write, binary
        with open('flightGroupData.pkl', 'wb') as FGhandler:
            pickle.dump(self, FGhandler)


   #Primarily for debugging, this will List the information the user gives in a easily readable format
    def printinfo(self):
        print("\n \n Your group consists of \n")
        for travelers in self.origins:
            print(travelers[1] + "  Travelers from " + travelers[0] + "\n")
        print("Your group will arrive in " + self.destination + " on " + self.departDate + "\n")
        print("And return on " +  self.returnDate + "\n")
import pickle

class flightGroup:
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, destination, dateLowerBound, dateUpperBound, stayRange, email, groupOrigins=None):
        # The __init__ function is the primary constructor for the class

        self.destination = destination          # The Destination the Flight Group is heading to        FORMAT (string):    "MSP"
        self.dateLowerBound = dateLowerBound    # The date the group would like to depart               FORMAT (string):    "YYYY-MM-DD" 
        self.dateUpperBound = dateUpperBound    # The date the group would like to return               FORMAT (string):    "YYYY-MM-DD"
        self.stayRange = stayRange              # The length the group would like to stay               FORMAT (tuple):     (INT, INT)
        self.email = email                      # The email address associated with the group           FORMAT (string):    "example@email.com"

        
        if groupOrigins is None:                # Home Airport-Passengers info                          FORMAT (list):      [("LAX", 3),...,("MAD", 5)]
            self.groupOrigins = []
        else: self.groupOrigins = groupOrigins

    

    # Save pickles the instance
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    def save(self): 
        with open('flightGroupData.pkl', 'ab') as FGhandler:
            pickle.dump(self, FGhandler)



    # printinfo prints all information about the current group in a readable format
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    def printinfo(self):
        print("Group Information: ")
        print("---------------------------------------------------------------------")
        print("Your group is interested in traveling to: " + self.destination)
        print("Sometime between " + str(self.dateLowerBound) + " and " + str(self.dateUpperBound))
        print("And you are interested in a stay of " + str(self.stayRange[0]) + " to " + str(self.stayRange[1]) + " days")
        print("Your contact email address is: " + self.email)
        print("---------------------------------------------------------------------")
        print("Traveler origins: ")
        for travelers in self.groupOrigins:
            print(str(travelers[1]) + "  Travelers from " + travelers[0])
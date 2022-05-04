import pickle

# The flightgroup class is the nucleus of the entire project, 
# it contains the core elements that we need to build out this project. 
# It contains only data points, constructors

#--------------------------------------------------------------------------------------------------------------------------------------------------

class flightGroup:

    # Class Variables
    #------------------------------------------------------------------

    groupNumber = 0 # Eventually, this will count the number of groups 
                    # total that we have added. It will then function
                    # as the Primary Key for finding info about particular
                    # groups within our table of group info
    

    # Constructor Methods
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, destination, departDate, returnDate, stayRange, email, groupOrigins=None):
        # The __init__ function is the primary constructor for the class

        self.destination = destination # The Destination the Flight Group is heading to
        self.departDate = departDate # The date the group would like to depart
        self.returnDate = returnDate # The date the group would like to return
        self.stayRange = stayRange # the length the group would like to stay
        self.email = email # email address associated with the group

        # A note on the above attributes. At current time stayrange will do nothing
        # eventually it should be saved, likely as a string, such that the user can
        # write x-y where (x,y) is a range of days (3 to 10 days).
        
        # Group origins will be a list, with elements in the form (str, int)
        # which will stand for (Airport Code, Number of fliers from this airport).
        
        # We default to an empty list if nothing is passed in here, otherwise we set origins to the passed list.
        # later I should check if this is necessary but for now it feels like what I ought to do.
        if groupOrigins is None:
            self.groupOrigins = []
        else: self.groupOrigins = groupOrigins

    #------------------------------------------------------------------------------------------

    # The following method will populate an instance of a class from a pickle file. For now, it will not be used
    # I believe the best course of action is to handle this from the handler
    

    # from_file I believe to be broken logic going forward as it opens and closes the file each time, and there is 
    # therefore no way to loop over the pickle jar. The Proper method should be to do this from the handler, creating a blank 
    # intance as temporary, loading it using the unpickler, pushing a copy of that temp onto the list of groups
    # and then rinsing and repeating. For now, it serves as a simple way to check whether or not the code is 
    # able to handle a single group being pickled and unpickled without error
    @classmethod
    def from_file(cls): # from_file populates an instance of a flight group from a serialized file
        #print("Beginning from_file constructor method" + "\n")
        with open('flightGroupData.pkl', 'rb') as FGhandler:
            a = pickle.load(FGhandler)
            print("\n")
            return a

    def save(self): # This function pickles the current group for future use
        #opens the file and prepares to write to it. 'wb' --> write, binary
        #print("Beginning save method" + "\n")
        with open('flightGroupData.pkl', 'ab') as FGhandler:
            pickle.dump(self, FGhandler)

    def printinfo(self):
        for travelers in self.groupOrigins:
            print(str(travelers[1]) + "  Travelers from " + travelers[0])
        print("Destination: " + self.destination)
        print("Date of Departure: " + self.departDate)
        print("Date of Return: " + self.returnDate)
        print("Email: " + self.email)
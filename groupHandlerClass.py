import pickle
from flightGroupClassMk2 import flightGroup

class handler:

    def __init__(self, group=None):
        if group == None:
            self.group = []
        else:
            self.group = group

    def load(self):
        with open('flightGroupData.pkl', 'rb') as filehandler:
            while True:
                try:
                     self.group.append(pickle.load(filehandler))
                except (EOFError, pickle.UnpicklingError):
                    print("End of file Reached")
                    break
    
    @staticmethod
    def printall(self):
        for members in self.group:
            print("-----------GROUP-------------")
            members.printinfo()


    
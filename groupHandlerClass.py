from ast import Pass
import pickle
import threading
import datetime
import time
import exampleGroupGenerator

from flightGroupClassMk2 import flightGroup

class handler:

    def __init__(self, groups=None):
        print("initializing")
        if groups == None:
            self.groups = []
        else:
            self.groups = groups
    
    
    # This FORMATS and rewrites the pickle file with 
    #def save(self):
    #    with open('flightGroupData.pkl', 'wb') as FGhandler:
     #       for i in self.groups:
     #          pickle.dump(i, FGhandler)
    
    def newGroup(self, fgroup):
        self.groups.append(fgroup)
    
@staticmethod
def printall(self):
    for members in self.groups:
        print("-----------GROUP-------------")
        members.printinfo()
        print("\n\n")

















# def fetchFlightPrices(flight, lower, upper):
#     #iterate over lower/upper date
#     span = toDateTime(lower, upper)

#     threads = []
#     start = time.perf_counter()
#     for day in span:
#         t = threading.Thread(target=callAPI, args=[flight, day])
#         t.start()
#         time.sleep(0.6)
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     finish = time.perf_counter()
#     print(f'Finished in {round(finish-start, 2)} second(s)' '')

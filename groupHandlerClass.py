from ast import Pass
import pickle
import threading
import datetime
import time
import exampleGroupGenerator

from flightGroupClassMk2 import flightGroup

class handler:

    def __init__(self, groups=None):
        if groups == None:
            self.groups = []
        else:
            self.groups = groups

    def newGroup(self, fgroup):
        self.groups.append(fgroup)
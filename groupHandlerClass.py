import flightGroupClassMk2 as fg
import pickle

class groupHandler:

    def __init__(self, group):
        self.group = group
    
    @classmethod
    def from_pickle(cls):
        groups = []
        with open('flightGroupData.pkl', 'rb') as unpickler:
            while True:
                try:
                    yield pickle.load(unpickler)
                except EOFError:
                        break
        cls.group = groups
        return (groups)

    @classmethod
    def reload(self):
        self.group = self.from_pickle()

    def PrintAll(self):
        for groups in self.group:
            groups.printinfo()

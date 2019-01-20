'''
Created on Jan 20, 2019

@author: drb116
'''

class Room:
    '''
    Holds details about a room and the connecting rooms
    '''
    

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.items = []
    
    def __str__(self):
        for_return = "You are in the {}.\n".format(self.name)
        if self.north !=None:
            for_return += "The %s is to the North.\n"%(self.north.name)
        if self.south !=None:
            for_return += "The %s is to the South.\n"%(self.south.name)
        if self.west !=None:
            for_return += "The %s is to the West.\n"%(self.west.name)
        if self.east !=None:
            for_return += "The %s is to the East.\n"%(self.east.name)
        return for_return
    
        
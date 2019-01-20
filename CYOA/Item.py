'''
Created on Jan 20, 2019

@author: drb116
'''

class Item:
    '''
    Item describes items found in various rooms and holds whether they are in the 
    user's inventory.
    '''
    def __init__(self, name,location):
        '''
        Constructor
        '''
        self.name = name
        self.location = location
        self.user_owns = False
        self.description = None
        
    def __str__(self):
        return "There is a {}\n".format(self.name)
        
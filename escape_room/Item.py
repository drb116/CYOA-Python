'''
Created on Jan 20, 2019

@author: drb116
'''

class Item(object):
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
        self.visible = True
        self.lookat = None
        self.use = None
        self.lookunder = None
        
    def __str__(self):
        return "There is a {}.\n".format(self.name)
        
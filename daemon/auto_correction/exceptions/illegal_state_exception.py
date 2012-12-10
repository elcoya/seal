'''
Created on 03/12/2012

@author: anibal
'''

class IllegalStateException(Exception):
    """Meant to be risen when a class is not in an appropiate state to be invoked."""


    def __init__(self, reason="No reason"):
        """Only constructor, needs an explanation of why it's risen."""
        self.reason = reason
    
    def __str__(self):
        return self.__class__.__name__ + " | reason: " + self.reason
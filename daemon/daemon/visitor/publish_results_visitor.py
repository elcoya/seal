'''
Created on 04/12/2012

@author: anibal
'''
from abc import abstractmethod

class PublishResultsVisitor:
    """
    
    Head of the visitor hierarchy. The visitors are in charge of publishing the
    results of the scripts run for the deliveries made.
    
    """
    
    @abstractmethod
    def visit(self, visitable):
        yield None

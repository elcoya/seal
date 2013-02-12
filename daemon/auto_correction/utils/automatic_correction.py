"""

@author: anibal

"""
import os

class AutomaticCorrection:
    """
    Utility bean to store the data associated with the automatic corrections handled by the daemon
    """

    def __init__(self, pk, script=None, delivery=None, delivery_id=None, captured_stdout=None, exit_value=None, status=None):
        self.pk = pk
        self.delivery_id = delivery_id
        self.captured_stdout = captured_stdout
        self.exit_value = exit_value
        self.status = status
        self.delivery = delivery
        self.script = script
    
    def __str__(self):
        delivery_filename = os.path.basename(self.delivery)
        return self.pk + " - " + delivery_filename
    
    def accept(self, visitor):
        visitor.visit(self)
    

from django.db import models
from seal.model.delivery import Delivery

class Autocheck(models.Model):
    """
    
    Autocheck objects are the entities which represents the automatic check that
    SEAL can run on the deliveries made by the Students.
    
    """
    
    STATUS_STRINGS = {-1:"failed", 0:"pending", 1:"successfull"}
    
    delivery = models.ForeignKey(Delivery, unique=True)
    captured_stdout = models.CharField(max_length=10240, blank=True)
    exit_value = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        """Stringify the Autocheck"""
        return ("Autocheck | exit value: " + str(self.exit_value) + " - status: " + self.status)
    
    def get_status(self):
        """Returns a status raw value as a human readable value"""
        return Autocheck.STATUS_STRINGS[self.status]
    
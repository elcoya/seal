from django.db import models
from seal.model.delivery import Delivery


class Correction(models.Model):
    """Correction or grade granted. 
    
    It is the grade granted by the Teacher to the Student and a comment giving
    feedback for the Delivery made by the latter.
    
    """
    
    publicComent = models.TextField(max_length=2000)
    privateComent = models.TextField(max_length=2000)
    note = models.FloatField()
    delivery = models.ForeignKey(Delivery)
    
    def __str__(self):
        """Stringify the Correction"""
        return (str(self.note) + " - " + self.publicComent)

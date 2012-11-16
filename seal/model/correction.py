from django.db import models
from seal.model.delivery import Delivery


class Correction(models.Model):
    """Correction or grade granted. 
    
    It is the grade granted by the Teacher to the Student and a comment giving
    feedback for the Delivery made by the latter.
    
    """
    
    publicComent = models.TextField(max_length=2000)
    """The feedback given for the Student"""
    
    privateComent = models.TextField(max_length=2000)
    """A comment that can be made to be seen only by the Teachers"""
    
    note = models.FloatField()
    """The grade granted for the Delivery"""
    
    delivery = models.ForeignKey(Delivery)
    """The delivery to which corresponds this correction"""
    
    def __str__(self):
        """Stringify the Correction"""
        return (str(self.note) + " - " + self.publicComent)

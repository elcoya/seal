from django.db import models
from seal.model import Student
from seal.model.innings import Innings

class Suscription(models.Model):
    """
    
    The Subscriptions are actually the reflection of the action, performed by a
    Student, of applying to be enrrolled to a given Course. It is not the 
    enrollement, only the request to be accepted. It can either be aproved or
    discarded.
    
    """
    
    inning = models.ForeignKey(Innings)
    student = models.ForeignKey(Student)
    state = models.CharField(max_length = 32)
    suscriptionDate = models.DateField()
    resolveDate = models.DateField(null=True)
    
    def __str__(self):
        """Stringify the Suscription"""
        return (str(self.pk))
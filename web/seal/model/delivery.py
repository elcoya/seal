from django.db import models
from seal.model import Student, Practice
from seal.utils import managepath

class Delivery(models.Model):
    """Delivery class.
    
    It is the object or artifact that the Student presents as his work for a
    given assignment. In this case it is considered required to be a zip 
    package.
     
    """
    file = models.FileField(upload_to=managepath.get_instance().get_delivery_path())
    student = models.ForeignKey(Student)
    practice = models.ForeignKey(Practice)
    deliverDate = models.DateField()
    
    def __str__(self):
        """Stringify the Delivery"""
        return (str(self.practice) + " - " + str(self.student) + " - " + str(self.deliverDate))
    
    def get_automatic_correction(self):
        if(self.automaticcorrection_set.all().exists()):
            return self.automaticcorrection_set.all()[0]
        else:
            return None

from django.db import models
from seal.model import Student, Practice

import os
(PRACTICE_FILE_PATH, FILE_PATH) = os.path.split(os.path.realpath(os.path.dirname(__file__)))

class Delivery(models.Model):
    """Delivery class.
    
    It is the object or artifact that the Student presents as his work for a
    given assignment. In this case it is considered required to be a zip 
    package.
     
    """
    
    file = models.FileField(upload_to=PRACTICE_FILE_PATH+"/Delivery_Files/")
    student = models.ForeignKey(Student)
    practice = models.ForeignKey(Practice)
    deliverDate = models.DateField()
    def __str__(self):
        """Stringify the Delivery"""
        return (str(self.practice) + " - " + str(self.student) + " - " + str(self.deliverDate))
    
    
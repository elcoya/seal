from django.db import models
from seal.model import Student,Practice

import os
(PRACTICE_FILE_PATH, FILE_PATH) = os.path.split(os.path.realpath(os.path.dirname(__file__)))

class Delivery(models.Model):
    file = models.FileField(upload_to=PRACTICE_FILE_PATH+"/Delivery_Files/")
    student = models.ForeignKey(Student)
    practice = models.ForeignKey(Practice)
    deliverDate = models.DateField()
    def __str__(self):
        return self.pk
    
    
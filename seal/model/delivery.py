from django.db import models
from seal.model.student import Student

class Delivery(models.Model):
    student = models.ForeignKey(Student)
    uid = models.IntegerField(unique=True)
    deliverDate = models.DateField()
    def __str__(self):
        return self.uid
from django.db import models
from seal.model import Student
# Create your models here.

class Delivery(models.Model):
    student = models.ForeignKey(Student,related_name="delivery_by_user")
    uid = models.IntegerField(unique=True)
    statement = models.CharField(max_length = 200)
    deliverDate = models.DateField()
    def __str__(self):
        return self.uid
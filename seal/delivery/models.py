from django.db import models
from seal import model
# Create your models here.

class Delivery(models.Model):
    student = models.ForeignKey(model.Student,related_name="delivery_by_user")
    uid = models.IntegerField(unique=True)
    statement = models.CharField(max_length = 200)
    deliverDate = models.DateField()
    def __str__(self):
        return self.uid
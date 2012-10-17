from django.db import models
# Create your models here.

class Delivery(models.Model):
    uid = models.IntegerField(unique=True)
    statement = models.CharField(max_length = 200)
    deliverDate = models.DateField()
    def __str__(self):
        return self.uid
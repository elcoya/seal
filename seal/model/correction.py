from django.db import models
from seal.model.delivery import Delivery


class Correction(models.Model):
    publicComent = models.TextField(max_length=2000)
    privateComent = models.TextField(max_length=2000)
    note = models.FloatField()
    delivery = models.ForeignKey(Delivery)
    
    def __str__(self):
        return (str(self.note) + " - " + self.publicComent)

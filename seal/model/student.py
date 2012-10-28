from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    uid = models.CharField(unique=True, max_length = 32)
    email = models.CharField(max_length = 90)
    def __str__(self):
        return self.name

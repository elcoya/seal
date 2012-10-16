from django.db import models
from seal.model.course import Course

class Student(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length = 100)
    uid = models.IntegerField(unique=True)
    email = models.CharField(max_length = 90)
    def __str__(self):
        return self.name    
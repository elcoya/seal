from django.db import models
from seal.model.course import Course
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length = 100)
    uid = models.CharField(unique=True, max_length = 32)
    email = models.CharField(max_length = 90)
    courses = models.ManyToManyField(Course, blank=True)
    user = models.OneToOneField(User, blank=True)
    
    def __str__(self):
        return self.name

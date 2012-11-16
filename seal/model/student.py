from django.db import models
from seal.model.course import Course
from django.contrib.auth.models import User

class Student(models.Model):
    """
    
    The Students are the people, undergraduates, who are taking a course and
    aim to pass the subject. This is one of the main entities of this software.
    They are supposed to register and apply to be enrolled in the Course they
    are taking. Once accepted, they can see their assignments, download their
    descriptions. Once they have solved them, they will perform a Delivery and
    expect the corresponding feedback or Correction.
    
    For the purpouse of authentication, a User, from the django.auth module is
    associated with them, granting them a username and password to login to the
    site.
    
    """
    
    name = models.CharField(max_length = 100)
    uid = models.CharField(unique=True, max_length = 32)
    email = models.CharField(max_length = 90)
    courses = models.ManyToManyField(Course, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """Stringify the Student"""
        return self.name


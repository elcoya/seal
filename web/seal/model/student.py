from django.db import models
from django.contrib.auth.models import User
from seal.model.teacher import Teacher
from seal.model.innings import Innings

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
    
    uid = models.CharField(unique=True, max_length = 32)
    innings = models.ManyToManyField(Innings, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    corrector = models.ForeignKey(Teacher, null=True, blank=True)
    
    def __str__(self):
        """Stringify the Student"""
        return self.uid
    
    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

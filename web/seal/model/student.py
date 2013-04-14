from django.db import models
from django.contrib.auth.models import User
from seal.model.teacher import Teacher
from seal.model.shift import Shift
from django.utils.encoding import smart_str

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
    
    uid = models.CharField(unique=True, max_length = 32,verbose_name="Padron")
    shifts = models.ManyToManyField(Shift, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    corrector = models.ForeignKey(Teacher, null=True, blank=True)
    
    def __str__(self):
        """Stringify the Student"""
        return self.uid
    
    def get_full_name(self):
        return smart_str(self.user.first_name + " " + self.user.last_name)
    
    def get_shift(self, course):
        for shift in self.shifts.all():
            if shift.course == course:
                return shift

'''
Created on 28/10/2012

@author: anibal
'''

from django.db import models
from seal.model.student import Student
from seal.model.course import Course

class Enrolled(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    def __str__(self):
        return self.course.__str__() + " - " + self.student.__str__()


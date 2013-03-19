from django.db import models
from seal.model.course import Course

'''
Created on 06/03/2013

@author: martin
'''
from django.utils.encoding import smart_str

class Shift(models.Model):
    '''
    classdocs
    '''
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
    
    class Meta:
        """Metadata class indicating how this objects must be unique"""
        unique_together = (("name", "course"),)
    
    def __str__(self):
        """Stringify the Course"""
        return smart_str(self.course.name + "-" + self.name)
    
    def get_students(self, uid=None, name=None, email=None):
        partial_query = self.student_set.all()
        if(uid):
            partial_query = partial_query.filter(uid=uid)
        if(name):
            partial_query = partial_query.filter(name=name)
        if(email):
            partial_query = partial_query.filter(email=email)
        return partial_query

    def get_students_count(self):
        return (self.student_set.count())
    
    def remove_student(self, student):
        self.student_set.remove(student)
        
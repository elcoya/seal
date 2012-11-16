from django.db import models
from seal.model.student import Student
from seal.model.course import Course

class Enrolled(models.Model):
    """
    
    In order to belong to a given Course, a Student must be enrolled in it.
    This class represents that relationship, and serves as a link between the
    Students and the Courses in which they are involved.
    
    """
    
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    
    def __str__(self):
        """Stringify the Enrollement"""
        return self.course.__str__() + " - " + self.student.__str__()


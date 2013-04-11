from django.db import models
from django.utils.encoding import smart_str

class Course(models.Model):
    """Course class representing a term
    
    The Course is understood as the series of lessons in the subject which sums
    up to be the whole content expected to be aquired by the students during
    their learning. It is concibed to last for one term (year, semester, etc)
    
    """
    
    name = models.CharField(max_length = 32, unique=True)
    
    def __str__(self):
        """Stringify the Course"""
        return smart_str(self.name)
    
    def student_count(self):
        shifts_query_set = self.shift_set.all()
        count = 0
        for shift in shifts_query_set:
            count += shift.student_set.all().count()
        return count
    
    def get_students(self, uid=None, name=None, email=None):
        partial_query = self.student_set.all()
        if(uid):
            partial_query = partial_query.filter(uid=uid)
        if(name):
            partial_query = partial_query.filter(name=name)
        if(email):
            partial_query = partial_query.filter(email=email)
        return partial_query
    
    def get_student_count(self):
        shifts = self.shift_set.all()
        total = 0;
        for shift in shifts:
            total = total + shift.student_set.count()
        return total
    
    def add_student(self, student):
        self.student_set.add(student)
    
    def remove_student(self, student):
        self.student_set.remove(student)
    
    def get_practices(self):
        return self.practice_set.all()
    
    class Meta:
        """
        Meta class to indicate the expected ordering of this objects when 
        querying on this class.
        """
        ordering = ('-name',)

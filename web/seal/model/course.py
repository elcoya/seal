from django.db import models

class Course(models.Model):
    """Course class representing a term
    
    The Course is understood as the series of lessons in the subject which sums
    up to be the whole content expected to be aquired by the students during
    their learning. It is concibed to last for one term (year, semester, etc)
    
    """
    
    name = models.CharField(max_length = 32, unique=True)
    
    def __str__(self):
        """Stringify the Course"""
        return self.name
    
    class Meta:
        """
        Meta class to indicate the expected ordering of this objects when 
        querying on this class.
        """
        ordering = ('-name',)
    
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
        return self.student_set.count()
    
    def add_student(self, student):
        self.student_set.add(student)
    
    def remove_student(self, student):
        self.student_set.remove(student)
    
    def get_practices(self):
        return self.practice_set.all()

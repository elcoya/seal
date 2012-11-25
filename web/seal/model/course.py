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

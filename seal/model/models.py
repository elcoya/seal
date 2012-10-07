from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 32)
    
    def __init__(self, nameToBeGiven):
        super(Course, self).__init__()
        self.name = nameToBeGiven
        
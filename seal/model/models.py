from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 32, unique=True)
    def __str__(self):
        return self.name
    
    
    
class Student(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length = 100)
    uid = models.IntegerField(unique=True)
    def __str__(self):
        return self.name
    
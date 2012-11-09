from django.db import models
from seal.model import Course, Student

class Suscription(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    state = models.CharField(max_length = 32)
    suscriptionDate = models.DateField()
    def __str__(self):
        return (str(self.pk))
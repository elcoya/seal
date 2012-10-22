from django.db import models
from seal.model.course import Course

class Practice(models.Model):
    uid = models.IntegerField(unique=True)
    course = models.ForeignKey(Course)
    statement = models.TextField()
    deadline = models.DateField()
    def __str__(self):
        return (str(self.uid)+"/"+self.course.name)
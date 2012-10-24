from django.db import models
from seal.model.course import Course

import os
(PRACTICE_FILE_PATH, FILE_PATH) = os.path.split(os.path.realpath(os.path.dirname(__file__)))

class Practice(models.Model):
    uid = models.IntegerField(unique=True)
    course = models.ForeignKey(Course)
    file = models.FileField(upload_to=PRACTICE_FILE_PATH+"/Practice_Files/")
    deadline = models.DateField()
    def __str__(self):
        return (str(self.uid)+"/"+self.course.name)
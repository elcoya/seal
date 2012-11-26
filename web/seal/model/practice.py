from django.db import models
from seal.model.course import Course

import os
(PRACTICE_FILE_PATH, FILE_PATH) = os.path.split(os.path.realpath(os.path.dirname(__file__)))
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('../../conf/local.cfg'))
BASE_PATH = config.get("Path", "path.workspace")

class Practice(models.Model):
    """Assignment.
    
    This class, probably poorly named, represents the assignments given to the
    Students to do in order to pass the Course.
    
    """
    
    uid = models.CharField(max_length=32)
    course = models.ForeignKey(Course)
    file = models.FileField(upload_to=BASE_PATH + "practice_files/")
    deadline = models.DateField()
    
    class Meta:
        """Metadata class indicating how this objects must be unique"""
        unique_together = (("uid", "course"),)
    
    def __str__(self):
        """Stringify the Practice or assignment"""
        return (str(self.uid))

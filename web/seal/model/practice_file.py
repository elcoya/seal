from django.db import models
from seal.model.practice import Practice
from seal.utils import managepath
import mimetypes

'''
Created on 23/02/2013

@author: martin
'''

TYPEEDITABLE = 'text'

class PracticeFile(models.Model):
    """
    
    This class is the holder for the practice file associated with each practice.
    
    """
    practice = models.ForeignKey(Practice)
    name =  models.CharField(max_length=32)
    file = models.FileField(upload_to=managepath.get_instance().get_practice_path())
    
    def __str__(self):
        """Stringify the Practice or assignment"""
        return (str(self.name))


    def isEditable(self):
        mime = str(mimetypes.guess_type(self.file.name)[0])
        pos = mime.find(TYPEEDITABLE)
        if (pos == 0):
            return True
        return False
        
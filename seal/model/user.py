'''
Created on 28/10/2012

@author: anibal
'''
from django.db import models
from django.contrib.auth.models import User

class SealUser(models.Model):
    user = models.ForeignKey(User)
    
    def authenticate(self, passwd):
        return True
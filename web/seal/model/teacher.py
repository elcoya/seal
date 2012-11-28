from django.db import models
from django.contrib.auth.models import User

MSGEXEPTION = 'Teacher cannot be saved without an authentication register.\
                Please, give the teacher an associated user so he can login.'

class Teacher(models.Model):
    """
    
    Professors or Teachers who dictates the lectures and grade the Students' 
    work are the target class of this application. They are in charge of 
    creating the assignments, evaluating them and giving feedback to the 
    Students who take their course. This is one of the profiles considered by 
    this application. For the purpouse of authentication, a User, from the 
    django.auth module is associated with them, granting them a username and
    password to login to the site.
    
    """
    
    name = models.CharField(max_length = 100)
    uid = models.CharField(unique=True, max_length = 32)
    email = models.CharField(max_length = 90)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """Stringify the Teacher"""
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None):
        """Extends parent. Checks for the existance of the login user"""
        if(self.user is None):
            raise Exception(msg=MSGEXEPTION)
        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using)

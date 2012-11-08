from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    uid = models.CharField(unique=True, max_length = 32)
    email = models.CharField(max_length = 90)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None):
        if(self.user is None):
            raise Exception(
                    msg='Teacher cannot be saved without an authentication register.'
                        + ' Please, give the teacher an associated user so he can login.')
        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using)

'''
Created on 06/12/2012

@author: martin
'''
from django import forms
from django.forms.forms import Form
from django.contrib.auth.models import User

ERRORUIDVALIDATION = "User not exist with this email"

class RecoveryForm(Form):
    uid = forms.CharField(max_length=32)
    email = forms.EmailField()
    
    def clean_uid(self):
        uid = self.data.get('uid','')
        email = self.data.get('email','')
        if(not (User.objects.filter(username = uid, email = email))):
            raise forms.ValidationError(ERRORUIDVALIDATION)

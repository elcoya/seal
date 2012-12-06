'''
Created on 06/12/2012

@author: martin
'''
from django import forms
from django.forms.forms import Form

class RecoveryForm(Form):
    uid = forms.CharField(max_length=32)
    email = forms.EmailField()
    
    
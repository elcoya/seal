'''
Created on 04/11/2012

@author: anibal
'''
from django import forms
from django.forms.forms import Form

class LoginForm(Form):
    """
    Registrtion form for new Student
    """
    name = forms.CharField(max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True))
    

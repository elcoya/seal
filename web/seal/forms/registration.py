'''
Created on 04/11/2012

@author: anibal
'''
from django import forms
from seal.model.student import Student
from django.forms.forms import Form
from seal.model.innings import Innings
from seal.model.teacher import Teacher

ERRORUIDVALIDATION = "User uid is not available"
ERRORPASSWDNOTMATCH = "Passwords does not match"

class RegistrationForm(Form):
    """
    Registrtion form for new Student
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    uid = forms.CharField(max_length=32)
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True))
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True))
    email = forms.EmailField()
    inning = forms.ModelChoiceField(queryset=Innings.objects.all() , empty_label="No Innings")
    
    def clean_uid(self):
        uid = self.cleaned_data['uid']
        if(Student.objects.filter(uid=uid) or Teacher.objects.filter(uid=uid)):
            raise forms.ValidationError(ERRORUIDVALIDATION)
    
    def clean_passwd_again(self):
        passwd = self.cleaned_data.get('passwd', None)
        passwd_again = self.cleaned_data.get('passwd_again', None)
        if(not (passwd == passwd_again)):
            raise forms.ValidationError(ERRORPASSWDNOTMATCH)

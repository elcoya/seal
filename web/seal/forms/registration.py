'''
Created on 04/11/2012

@author: anibal
'''
from django import forms
from seal.model.student import Student
from django.forms.forms import Form

class RegistrationForm(Form):
    """
    Registrtion form for new Student
    """
    name = forms.CharField(max_length=100)
    uid = forms.CharField(max_length=32)
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True))
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True))
    email = forms.EmailField()
    
    def clean_uid(self):
        uid = self.cleaned_data['uid']
        if(Student.objects.filter(uid=uid)):
            raise forms.ValidationError("User '" + uid + "' is not available")
    
    def clean_passwd_again(self):
        passwd = self.cleaned_data['passwd']
        passwd_again = self.cleaned_data['passwd_again']
        if(not (passwd == passwd_again)):
            raise forms.ValidationError("Passwords does not match")

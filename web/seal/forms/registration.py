'''
Created on 04/11/2012

@author: anibal
'''
from django import forms
from seal.model.student import Student
from django.forms.forms import Form
from seal.model.shift import Shift
from seal.model.teacher import Teacher
from cProfile import label
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

ERRORUIDVALIDATION = _("uidNotAvaible")
ERRORPASSWDNOTMATCH = _("passwordNotMatch")

class RegistrationForm(Form):
    """
    Registrtion form for new Student
    """
    first_name = forms.CharField(max_length=100, label=_("name"))
    last_name = forms.CharField(max_length=100, label=_("lastName"))
    uid = forms.CharField(max_length=32, label=_("uidRegistration"))
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), label=_("password"))
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), label=_("repeatPassword"))
    email = forms.EmailField()
    shifts = forms.ModelChoiceField(queryset=Shift.objects.all() , empty_label=_("emptyLabelRegistration"), label=_("shift"))
    
    def clean_uid(self):
        uid = self.cleaned_data['uid']
        if(User.objects.filter(username=uid)):
            raise forms.ValidationError(ERRORUIDVALIDATION)
    
    def clean_passwd_again(self):
        passwd = self.cleaned_data.get('passwd', None)
        passwd_again = self.cleaned_data.get('passwd_again', None)
        if(not (passwd == passwd_again)):
            raise forms.ValidationError(ERRORPASSWDNOTMATCH)

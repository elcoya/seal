'''
Created on 06/12/2012

@author: martin
'''
from django import forms
from django.forms.forms import Form
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

ERRORUIDVALIDATION = _("userPasswordNotExist")
ERRORPASSWDNOTMATCH = _("passwordsNotMatch")

class ChangePasswForm(Form):
    uid = forms.CharField(max_length=32, label=_("uidChangePassword"))
    oldpasswd = forms.CharField(widget=forms.PasswordInput(render_value=True), label=_("oldPassword"))
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), label=_("newPassword"))
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), label=_("repeatPassword"))
    
    def clean_uid(self):
        uid = self.cleaned_data['uid']
        if(not (User.objects.filter(username=uid))):
            raise forms.ValidationError(ERRORUIDVALIDATION)
        else:
            user = User.objects.get(username=uid)
            if (not user.check_password(self.data['oldpasswd'])):
                raise forms.ValidationError(ERRORUIDVALIDATION)
    
    def clean_passwd_again(self):
        passwd = self.cleaned_data.get('passwd', None)
        passwd_again = self.cleaned_data.get('passwd_again', None)
        if(not (passwd == passwd_again)):
            raise forms.ValidationError(ERRORPASSWDNOTMATCH)

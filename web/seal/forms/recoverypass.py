'''
Created on 06/12/2012

@author: martin
'''
from django import forms
from django.forms.forms import Form
from django.contrib.auth.models import User
from cProfile import label
from django.utils.translation import ugettext as _

ERRORUIDVALIDATION = _("notExistUserEmail")

class RecoveryForm(Form):
    uid = forms.CharField(max_length=32, label=_("uidRecoveryPassword"))
    email = forms.EmailField()
    
    def clean_uid(self):
        uid = self.data.get('uid','')
        email = self.data.get('email','')
        if(not (User.objects.filter(username = uid, email = email))):
            raise forms.ValidationError(_(ERRORUIDVALIDATION))

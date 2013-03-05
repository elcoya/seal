from django import forms
from seal.model.teacher import Teacher
from django.contrib.auth.models import User
from django.forms.models import ModelForm

ERRORNOPASSWD = "A password must be supplied"
ERRORPASSWDNOTMATCH = "Passwords does not match"

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)
        
    username = forms.CharField(max_length=100) 
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)
    
    def clean_passwd(self):
        uid = self.cleaned_data.get('uid', None)
        username = self.cleaned_data.get('username', None)
        passwd = self.cleaned_data['passwd']
        if (uid is not None):
            if((not (User.objects.filter(username = username).exists())) and (passwd == '')):
                raise forms.ValidationError(ERRORNOPASSWD)

    def clean_passwd_again(self):
        passwd = self.data['passwd']
        passwd_again = self.cleaned_data['passwd_again']
        if((passwd or passwd_again) and (not (passwd == passwd_again)) ):
            raise forms.ValidationError(ERRORPASSWDNOTMATCH)
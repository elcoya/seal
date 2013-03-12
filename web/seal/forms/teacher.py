from django import forms
from seal.model.teacher import Teacher
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from cProfile import label

ERRORNOPASSWD = "A password must be supplied"
ERRORPASSWDNOTMATCH = "Passwords does not match"
ERRORUSERDVALIDATION = "Username is not available"

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)
        
    username = forms.CharField(max_length=100, label="Usuario") 
    first_name = forms.CharField(max_length=100, label="Nombre Completo")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Email")
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False, label="Password")
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False, label="Repetir Password")
        
    def clean_username(self):
        uid = self.cleaned_data.get('uid', None)
        username = self.cleaned_data.get('username', None)
        if(User.objects.filter(username=username).exists() and not (Teacher.objects.filter(uid=uid).exists())):
            raise forms.ValidationError(ERRORUSERDVALIDATION)
    
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

class TeacherModifForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)
        
    username = forms.CharField(max_length=100, label="Usuario") 
    first_name = forms.CharField(max_length=100, label="Nombre Completo")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Email")
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False, label="Password")
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False, label="Repetir Password")
        
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
                 
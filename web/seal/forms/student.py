from django.forms import ModelForm
from seal.model.student import Student
from django import forms
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)
    
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)
    passwd_again = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)
    
    def clean_passwd(self):
        uid = self.cleaned_data['uid']
        passwd = self.cleaned_data['passwd']
        if((not (User.objects.filter(username=uid).exists())) and (passwd=='')):
            raise forms.ValidationError("A password must be supplied")

    def clean_passwd_again(self):
        passwd = self.data['passwd']
        passwd_again = self.cleaned_data['passwd_again']
        if((passwd or passwd_again) and (not (passwd == passwd_again)) ):
            raise forms.ValidationError("Passwords does not match")
        uid = self.cleaned_data['uid']
        if(User.objects.filter(username=uid).exists()):
            user = User.objects.get(username=uid)
            if(not passwd==''):
                user.set_password(passwd)
                user.save()
        else:
            user = User()
            user.username = uid
            user.set_password(passwd)
            user.save()
        self.instance.user = user
    

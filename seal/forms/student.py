from django.forms import ModelForm
from seal.model.student import Student
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
    
    email = forms.EmailField()
    

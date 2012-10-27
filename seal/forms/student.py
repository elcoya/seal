from django.forms import ModelForm
from django.forms import forms
from seal.model.practice import Practice
from seal.model.student import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student

from django.forms import ModelForm
from django.forms import forms
from seal.model.course import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
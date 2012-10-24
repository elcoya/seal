from django.forms import ModelForm
from django.forms import forms
from seal.model.practice import Practice

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
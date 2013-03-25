from django.forms import ModelForm
#from django.forms import forms
from seal.model.practice import Practice

#ERRORTYPEPERMITED = "Only pdf is permited to upload!"
#TYPEPDF = "application/pdf"

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
from django.forms import ModelForm
from django.forms import forms
from seal.model.practice import Practice

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        
    def clean_file(self):
        data = self.cleaned_data['file']
        ext = data.content_type
        if (ext != "application/pdf"):
            raise forms.ValidationError("Only pdf is permited to upload!")
        return data
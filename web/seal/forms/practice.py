from django.forms import ModelForm
from django.forms import forms
from seal.model.practice import Practice

ERRORTYPEPERMITED = "Only pdf is permited to upload!"
TYPEPDF = "application/pdf"

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        
    def clean_file(self):
        data = self.cleaned_data['file']
        try:
            ext = data.content_type
            if (ext != TYPEPDF):
                raise forms.ValidationError(ERRORTYPEPERMITED)
        except AttributeError:
            pass  
        return data
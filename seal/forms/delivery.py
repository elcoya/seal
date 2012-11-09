from django.forms import ModelForm
from django.forms import forms
from seal.model import Delivery

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ('student', 'practice', 'deliverDate',)
        
    def clean_file(self):
        data = self.cleaned_data['file']
        ext = data.content_type
        if (ext != "application/zip" or ext != "application/octet-stream"):
            error = "Only zip is permited to upload!"
            raise forms.ValidationError(error)
        return data
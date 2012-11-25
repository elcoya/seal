from django.forms import ModelForm
from django.forms import forms
from seal.model import Delivery
import os

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ('student', 'practice', 'deliverDate',)
        
    def clean_file(self):
        data = self.cleaned_data['file']
        detected_type = data.content_type
        filename = data.name
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        if ((detected_type in ("application/zip", "application/x-zip-compressed")) or 
            (detected_type == "application/octet-stream" and ext == ".zip")):
            return data
        else:
            error = "Only zip is permited to upload! Type detected: " + str(detected_type)
            raise forms.ValidationError(error)
        
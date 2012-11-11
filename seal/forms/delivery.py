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
        tipe = data.content_type
        filename = data.name
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        print(ext)
        if ((tipe in ("application/zip", "application/x-zip-compressed")) or (tipe == "application/octet-stream" and ext == ".zip")):
            return data
        else:
            error = "Only zip is permited to upload! Type detected: " + str(tipe)
            raise forms.ValidationError(error)
        
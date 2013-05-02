from django.forms import ModelForm
from django.forms import forms
from seal.model import Delivery
import os
from django.utils.translation import ugettext as _

ERRORTYPEPERMITED = _("errorOnlyZip")
TYPEZIP = "application/zip"
TYPEXZIP = "application/x-zip-compressed"
TYPEOCTETSTREAM = "application/octet-stream"
EXTENTIONPERMITED = ".zip"

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ('student', 'practice', 'deliverDate','corrector')
        
    def clean_file(self):
        data = self.cleaned_data['file']
        detected_type = data.content_type
        filename = data.name
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        if ((detected_type in (TYPEZIP, TYPEXZIP)) or 
            (detected_type == TYPEOCTETSTREAM and ext == EXTENTIONPERMITED)):
            return data
        else:
            raise forms.ValidationError(ERRORTYPEPERMITED)
        
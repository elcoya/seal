from django.forms import ModelForm
from django.utils.translation import ugettext as _
from seal.model.practice import Practice
from datetime import date
from django import forms

ERRORDATEFUTURE = _("The deadline should be in the future")
ERRORDATEFORMAT = _("Invalid date, date should be in format yyyy-mm-dd")
ERRORNAME = _("Name cannot be blank")

class PracticeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PracticeForm, self).__init__(*args, **kwargs)
        self.fields['uid'].error_messages['required'] = ERRORNAME
        self.fields['deadline'].error_messages['invalid'] = ERRORDATEFORMAT
    
    class Meta:
        model = Practice
        exclude = ('course',)
        
    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        today = date(date.today().year, date.today().month, date.today().day)
        if (deadline <= today):
            raise forms.ValidationError(ERRORDATEFUTURE)
        else:
            return deadline
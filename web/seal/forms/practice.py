from django.forms import ModelForm
from django.utils.translation import ugettext as _
from seal.model.practice import Practice
from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from seal.model.course import Course

ERRORDATEFUTURE = _("errorDeadlineFuture")
ERRORDATEFORMAT = _("errorInvalidFormatDate")
ERRORNAME = _("errorNameNotBlank")

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
                
    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        exclude.remove('course') # allow checking against the missing attribute
        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError, e:
            self._update_errors(e.message_dict)

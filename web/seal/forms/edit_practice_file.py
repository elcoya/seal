"""

@author: anibal

"""
from django import forms

class EditPracticeFileForm(forms.Form):
    
    content = forms.Textarea(attrs={'cols': 80, 'rows': 40})
    
#    def __init__(self, *args, **kwargs):
#        super(EditPracticeFileForm, self).__init__(self, *args, **kwargs)
    

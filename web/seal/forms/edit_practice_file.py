"""

@author: anibal

"""
from django import forms

class EditPracticeFileForm(forms.Form):
    
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 25}), label='')
    

from django.forms import ModelForm
from seal.model.practice_file import PracticeFile

'''
Created on 23/02/2013

@author: martin
'''

class PracticeFileForm(ModelForm):
    class Meta:
        model = PracticeFile
        exclude = ('practice', )
    
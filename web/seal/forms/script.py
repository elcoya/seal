from django.forms import ModelForm
from seal.model.script import Script

class PracticeScriptForm(ModelForm):
    class Meta:
        model = Script
        exclude = ('practice', )
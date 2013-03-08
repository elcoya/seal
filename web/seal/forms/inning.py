from django.forms import ModelForm
from seal.model.innings import Innings

class InningForm(ModelForm):
    class Meta:
        model = Innings
    
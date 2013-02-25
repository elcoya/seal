from django.forms import ModelForm
from seal.model import Correction


class CorrectionForm(ModelForm):
    
    class Meta:
        model = Correction
        exclude = ('delivery', 'corrector')
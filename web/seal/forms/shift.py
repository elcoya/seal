from django.forms import ModelForm
from seal.model.shift import Shift

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
    
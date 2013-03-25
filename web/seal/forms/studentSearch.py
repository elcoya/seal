from django.forms.forms import Form
from django import forms

#ESTADOS = (("uid", "Padron"), ("name", "Nombre"))

class StudentSearchForm(Form):
    #criteria_search =  forms.ChoiceField(widget=forms.RadioSelect, choices=ESTADOS, label = "", required=True)
    data_search = forms.CharField(max_length=100, label="")

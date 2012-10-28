from django.forms import ModelForm
from seal.model.student import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student

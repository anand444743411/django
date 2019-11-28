from django import forms
from APP.models import Emp



class EmpForm(forms.ModelForm):
    class Meta:
        model =Emp
        fields = '__all__'
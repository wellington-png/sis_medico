from django import forms
from mediflow.apps.users.models import DoctorModel

class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorModel
        fields = ['crm', 'especiality']
        widgets = {
            'crm': forms.TextInput(attrs={'class': 'form-control'}),
            'especiality': forms.TextInput(attrs={'class': 'form-control'}),
        }

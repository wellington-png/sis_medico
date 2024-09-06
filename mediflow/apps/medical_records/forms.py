from django import forms
from .models import MedicalRecordModel

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecordModel
        fields = ['patient', 'doctor', 'diagnosis', 'prescription', 'documents']

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter diagnosis'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter prescription'}),
            'documents': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].widget.attrs.update({'class': 'form-control'})
        self.fields['doctor'].widget.attrs.update({'class': 'form-control'})
        self.fields['diagnosis'].widget.attrs.update({'class': 'form-control'})
        self.fields['prescription'].widget.attrs.update({'class': 'form-control'})
        self.fields['documents'].widget.attrs.update({'class': 'form-control-file'})

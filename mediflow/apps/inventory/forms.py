from django import forms
from .models import InventoryModel

class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryModel
        fields = ['name', 'quantity', 'minimum_quantity']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Enter quantity'}),
            'minimum_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Enter minimum quantity'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['minimum_quantity'].widget.attrs.update({'class': 'form-control'})

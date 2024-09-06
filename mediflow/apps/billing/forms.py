from django import forms
from .models import BillingModel, PaymentModel

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingModel
        fields = ['patient', 'appointment', 'amount', 'payment_status', 'payment_date']
        
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'appointment': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Enter amount'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ['invoice', 'payment_method', 'amount']
        
        widgets = {
            'invoice': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Enter amount'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['invoice'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})

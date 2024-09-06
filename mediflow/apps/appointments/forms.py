from django import forms
from .models import AppointmentModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = ["patient", "doctor", "description", "notes", "appointment_date"]

        widgets = {
            "patient": forms.Select(attrs={"class": "form-control"}),
            "doctor": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter description of the appointment",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Optional notes",
                }
            ),
            "appointment_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

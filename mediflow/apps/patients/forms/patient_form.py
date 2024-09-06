from django import forms
from mediflow.apps.users.models import UserModel
from mediflow.apps.patients.models import PatientModel


class PatientForm(forms.ModelForm):
    # Campos relacionados ao usuário
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = PatientModel
        fields = [
            "cpf",
            "name",
            "birth_date",
            "gender",
            "phone",
            "email",
            "address",
            "medical_history",
            "observations",
        ]
        widgets = {
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "medical_history": forms.Textarea(attrs={"class": "form-control"}),
            "observations": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        patient = super().save(commit=False)
        if not patient.user:
            user = UserModel.objects.create(
                username=self.cleaned_data["email"],  # Use email as the username
                email=self.cleaned_data["email"],
                first_name=self.cleaned_data["name"].split()[0],
                last_name=" ".join(self.cleaned_data["name"].split()[1:]),
                role="patient",
            )
            if self.cleaned_data.get("password1"):
                user.set_password(self.cleaned_data["password1"])
            else:
                user.set_unusable_password()  # Ou defina uma senha padrão se necessário
            user.save()
            patient.user = user

        if commit:
            patient.save()
        return patient

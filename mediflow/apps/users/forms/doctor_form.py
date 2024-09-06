from django import forms
from mediflow.apps.users.models import UserModel, DoctorModel


class DoctorForm(forms.ModelForm):
    # User-related fields
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    # Doctor-related fields
    crm = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    especiality = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = DoctorModel
        fields = ["crm", "especiality"]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            # If updating an existing instance
            self.fields["username"].initial = self.instance.user.username
            self.fields["email"].initial = self.instance.user.email
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
        else:
            # If creating a new instance
            self.fields["username"].initial = ""
            self.fields["email"].initial = ""
            self.fields["first_name"].initial = ""
            self.fields["last_name"].initial = ""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = (
            self.instance.user
            if self.instance.pk and self.instance.user
            else UserModel()
        )
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.role = "doctor"  # Fix the role to "doctor"

        if self.cleaned_data.get("password1"):
            user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            doctor = super(DoctorForm, self).save(commit=False)
            doctor.user = user
            if commit:
                doctor.save()
        return doctor

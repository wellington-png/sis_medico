from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mediflow.apps.patients.models import PatientModel
from mediflow.apps.patients.forms.patient_form import PatientForm


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = PatientModel
    form_class = PatientForm
    template_name = "patients/patient_form.html"
    success_url = reverse_lazy("patient-list")
    login_url = "/login/"

    def form_valid(self, form):
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = PatientModel
    form_class = PatientForm
    template_name = "patients/patient_form.html"
    success_url = reverse_lazy("patient-list")
    login_url = "/login/"

    def form_valid(self, form):
        return super().form_valid(form)


class PatientListView(LoginRequiredMixin, ListView):
    model = PatientModel
    template_name = "patients/patient_list.html"
    context_object_name = "patients"
    login_url = "/login/"

    def get_queryset(self):
        return PatientModel.objects.all().order_by("name")

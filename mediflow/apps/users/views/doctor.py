from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mediflow.apps.users.models import DoctorModel

from django.views.generic.edit import CreateView, UpdateView
from mediflow.apps.users.forms.doctor_form import DoctorForm


class DoctorListView(LoginRequiredMixin, ListView):
    model = DoctorModel
    template_name = "doctors/doctor_list.html"
    context_object_name = "doctors"
    login_url = "/login/"


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = DoctorModel
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = "/doctors/"
    login_url = "/login/"


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = DoctorModel
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = "/doctors/"
    login_url = "/login/"

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from mediflow.apps.users.models import UserModel
from mediflow.apps.users.forms.user_form import UserForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(LoginRequiredMixin, CreateView):
    model = UserModel
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("home")
    login_url = "/login/"

    def form_valid(self, form):
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("home")
    login_url = "/login/"

    def get_object(self, queryset=None):
        return UserModel.objects.get(pk=self.kwargs["pk"])

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.role == 'admin':
            form.fields['role'].disabled = True
        return form

    def form_valid(self, form):
        if not self.request.user.role == 'admin':
            form.instance.role = self.get_object().role 
        return super().form_valid(form)


class AdminListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = "users/admin_list.html"
    context_object_name = "users"
    login_url = "/login/"

    def get_queryset(self):
        return UserModel.objects.filter(role="admin")


class DoctorListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = "users/doctor_list.html"
    context_object_name = "users"
    login_url = "/login/"

    def get_queryset(self):
        return UserModel.objects.filter(role="doctor")


class ReceptionistListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = "users/receptionist_list.html"
    context_object_name = "users"
    login_url = "/login/"

    def get_queryset(self):
        return UserModel.objects.filter(role="receptionist")


class PatientListView(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = "users/patient_list.html"
    context_object_name = "users"
    login_url = "/login/"

    def get_queryset(self):
        return UserModel.objects.filter(role="patient")

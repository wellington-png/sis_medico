from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from .models import MedicalRecordModel
from .forms import MedicalRecordForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MedicalRecordListView(LoginRequiredMixin, ListView):
    model = MedicalRecordModel
    template_name = 'medical_records/medicalrecord_list.html'
    context_object_name = 'medical_records'
    login_url = '/login/'

class MedicalRecordCreateView(LoginRequiredMixin, CreateView):
    model = MedicalRecordModel
    form_class = MedicalRecordForm
    template_name = 'medical_records/medicalrecord_form.html'
    success_url = reverse_lazy('medicalrecord-list')
    login_url = '/login/'

class MedicalRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = MedicalRecordModel
    form_class = MedicalRecordForm
    template_name = 'medical_records/medicalrecord_form.html'
    success_url = reverse_lazy('medicalrecord-list')
    login_url = '/login/'

    def get_object(self):
        return get_object_or_404(MedicalRecordModel, pk=self.kwargs['pk'])

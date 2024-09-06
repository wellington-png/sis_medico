from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http import JsonResponse
from django.views import View


from .models import AppointmentModel
from .forms import AppointmentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = AppointmentModel
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointment-list")
    login_url = "/login/"

    def form_valid(self, form):
        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = AppointmentModel
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointment-list")
    login_url = "/login/"

    def form_valid(self, form):
        return super().form_valid(form)


class AppointmentListView(LoginRequiredMixin, ListView):
    model = AppointmentModel
    template_name = "appointments/appointment_list.html"
    context_object_name = "appointments"
    login_url = "/login/"
    paginate_by = 10  # Para paginação, se necessário

    def get_queryset(self):
        return AppointmentModel.objects.all().order_by("appointment_date")



class AppointmentCalendarView(View):
    def get(self, request, *args, **kwargs):
        appointments = AppointmentModel.objects.all()
        events = []
        for appointment in appointments:
            events.append({
                'title': f'{appointment.patient} - {appointment.doctor}',
                'start': appointment.appointment_date.strftime('%Y-%m-%d'),
                'url': reverse_lazy('appointment-update', args=[appointment.id]),
            })
        return JsonResponse(events, safe=False)


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AppointmentCalendarPageView(LoginRequiredMixin, TemplateView):
    template_name = 'appointments/appointment_calendar.html'
    login_url = '/login/'
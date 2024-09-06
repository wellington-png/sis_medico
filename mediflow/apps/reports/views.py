from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count, Sum
from mediflow.apps.appointments.models import AppointmentModel
from mediflow.apps.patients.models import PatientModel
from mediflow.apps.billing.models import BillingModel


class ReportView(TemplateView):
    template_name = 'reports/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Número total de consultas
        total_appointments = AppointmentModel.objects.count()
        
        # Número total de pacientes atendidos
        total_patients = PatientModel.objects.count()
        
        # Faturamento total
        total_billing = BillingModel.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        
        # Número de consultas por paciente
        appointments_per_patient = AppointmentModel.objects.values('patient').annotate(count=Count('id')).order_by('-count')
        
        # Número de consultas por médico
        appointments_per_doctor = AppointmentModel.objects.values('doctor').annotate(count=Count('id')).order_by('-count')
        
        # Faturamento por status de pagamento
        billing_status_summary = BillingModel.objects.values('payment_status').annotate(total_amount=Sum('amount'))
        
        context.update({
            'total_appointments': total_appointments,
            'total_patients': total_patients,
            'total_billing': total_billing,
            'appointments_per_patient': appointments_per_patient,
            'appointments_per_doctor': appointments_per_doctor,
            'billing_status_summary': billing_status_summary,
        })
        
        return context

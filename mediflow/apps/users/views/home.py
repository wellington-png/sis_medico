from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Count, Sum
from mediflow.apps.patients.models import PatientModel
from mediflow.apps.appointments.models import AppointmentModel
from mediflow.apps.inventory.models import InventoryModel
from mediflow.apps.billing.models import BillingModel
from mediflow.apps.medical_records.models import MedicalRecordModel

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "users/home.html"
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dados para cards
        context['total_patients'] = PatientModel.objects.count()
        context['total_appointments'] = AppointmentModel.objects.count()
        context['total_inventory_items'] = InventoryModel.objects.count()
        context['total_billing'] = BillingModel.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        # Dados para listagens
        context['recent_appointments'] = AppointmentModel.objects.order_by('-appointment_date')[:5]
        context['recent_bills'] = BillingModel.objects.order_by('-created_at')[:5]

        # Dados para gráficos
        context['appointment_counts'] = AppointmentModel.objects.values('appointment_date').annotate(count=Count('id'))
        context['billing_amounts'] = BillingModel.objects.values('payment_date').annotate(total_amount=Sum('amount'))

        if self.request.user.role == 'patient':
            try:
                patient = PatientModel.objects.get(user=self.request.user)
                context['medical_records'] = MedicalRecordModel.objects.filter(patient=patient)
            except PatientModel.DoesNotExist:
                context['medical_records'] = []

        return context
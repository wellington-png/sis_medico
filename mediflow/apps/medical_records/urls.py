from django.urls import path
from .views import MedicalRecordListView, MedicalRecordCreateView, MedicalRecordUpdateView

urlpatterns = [
    path('', MedicalRecordListView.as_view(), name='medicalrecord-list'),
    path('create/', MedicalRecordCreateView.as_view(), name='medicalrecord-create'),
    path('update/<int:pk>/', MedicalRecordUpdateView.as_view(), name='medicalrecord-update'),
]

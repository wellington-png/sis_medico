from django.urls import path


from mediflow.apps.patients.views import PatientCreateView, PatientUpdateView, PatientListView


urlpatterns = [
    path("create/", PatientCreateView.as_view(), name="patient-create"),
    path("update/<int:pk>/", PatientUpdateView.as_view(), name="patient-edit"),
    path("", PatientListView.as_view(), name="patient-list"),
]

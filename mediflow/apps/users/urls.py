from django.urls import path
from mediflow.apps.users.views import MyLoginView, HomeView, UserCreateView
from mediflow.apps.users.views import (
    AdminListView,
    DoctorListView,
    ReceptionistListView,
    PatientListView,
    UserUpdateView,
)


urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("", HomeView.as_view(), name="home"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("users/admins/", AdminListView.as_view(), name="admin-list"),
    path("users/doctors/", DoctorListView.as_view(), name="doctor-list"),
    path(
        "users/receptionists/", ReceptionistListView.as_view(), name="receptionist-list"
    ),
    path("users/patients/", PatientListView.as_view(), name="patient-list"),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="user-edit"),
]

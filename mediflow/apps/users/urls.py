from django.urls import path
from mediflow.apps.users.views import (
    AdminListView,
    ReceptionistListView,
    UserUpdateView,
    MyLoginView,
    MyLogoutView,
    HomeView,
    UserCreateView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorListView,
)

from .views import DoctorListView, DoctorCreateView, DoctorUpdateView


urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("", HomeView.as_view(), name="home"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("users/admins/", AdminListView.as_view(), name="admin-list"),
    path(
        "users/receptionists/", ReceptionistListView.as_view(), name="receptionist-list"
    ),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="user-edit"),
    path("doctors/", DoctorListView.as_view(), name="doctor-list"),
    path("doctor/create/", DoctorCreateView.as_view(), name="doctor-create"),
    path("doctor/update/<int:pk>/", DoctorUpdateView.as_view(), name="doctor-edit"),
]

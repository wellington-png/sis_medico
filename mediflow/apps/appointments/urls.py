from django.urls import path

from .views import (
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentListView,
    AppointmentCalendarView,
    AppointmentCalendarPageView,
)

urlpatterns = [
    path("create/", AppointmentCreateView.as_view(), name="appointment-create"),
    path(
        "<int:pk>/update/", AppointmentUpdateView.as_view(), name="appointment-update"
    ),
    path("", AppointmentListView.as_view(), name="appointment-list"),
    path(
        "calendar/",
        AppointmentCalendarPageView.as_view(),
        name="appointment-calendar-page",
    ),
    path(
        "calendar/data/",
        AppointmentCalendarView.as_view(),
        name="appointment-calendar-data",
    ),
]

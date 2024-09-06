from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATIC_ROOT},
    ),
    path("", include("mediflow.apps.users.urls")),
    path("patients/", include("mediflow.apps.patients.urls")),
    path("appointments/", include("mediflow.apps.appointments.urls")),
    path("medical-records/", include("mediflow.apps.medical_records.urls")),
    path("inventory/", include("mediflow.apps.inventory.urls")),
    path("", include("mediflow.apps.billing.urls")),
    path("reports/", include("mediflow.apps.reports.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

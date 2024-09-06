from django.urls import path
from .views import (
    BillingListView, BillingCreateView, BillingUpdateView, BillingDetailView,
    PaymentListView, PaymentCreateView, PaymentUpdateView
)

urlpatterns = [
    # Billing URLs
    path('billing/', BillingListView.as_view(), name='billing-list'),
    path('billing/create/', BillingCreateView.as_view(), name='billing-create'),
    path('billing/update/<int:pk>/', BillingUpdateView.as_view(), name='billing-update'),
    path('billing/<int:pk>/', BillingDetailView.as_view(), name='billing-detail'),
    
    # Payment URLs
    path('payment/', PaymentListView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(), name='payment-update'),
]
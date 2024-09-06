from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import PaymentModel, BillingModel
from .forms import PaymentForm, BillingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class PaymentListView(LoginRequiredMixin, ListView):
    model = PaymentModel
    template_name = "payment/payment_list.html"
    context_object_name = "payments"
    login_url = "/login/"


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = PaymentModel
    form_class = PaymentForm
    template_name = "payment/payment_form.html"
    success_url = reverse_lazy("payment-list")
    login_url = "/login/"


class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = PaymentModel
    form_class = PaymentForm
    template_name = "payment/payment_form.html"
    success_url = reverse_lazy("payment-list")
    login_url = "/login/"


class BillingListView(LoginRequiredMixin, ListView):
    model = BillingModel
    template_name = "billing/billing_list.html"
    context_object_name = "billings"
    login_url = "/login/"


class BillingCreateView(LoginRequiredMixin, CreateView):
    model = BillingModel
    form_class = BillingForm
    template_name = "billing/billing_form.html"
    success_url = reverse_lazy("billing-list")
    login_url = "/login/"


class BillingUpdateView(LoginRequiredMixin, UpdateView):
    model = BillingModel
    form_class = BillingForm
    template_name = "billing/billing_form.html"
    success_url = reverse_lazy("billing-list")
    login_url = "/login/"


class BillingDetailView(LoginRequiredMixin, DetailView):
    model = BillingModel
    template_name = "billing/billing_detail.html"
    context_object_name = "billing"
    login_url = "/login/"

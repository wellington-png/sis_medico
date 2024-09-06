from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from .models import InventoryModel
from .forms import InventoryForm
from django.contrib.auth.mixins import LoginRequiredMixin

class InventoryListView(LoginRequiredMixin, ListView):
    model = InventoryModel
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'
    login_url = '/login/'

class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = InventoryModel
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory-list')
    login_url = '/login/'

class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = InventoryModel
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory-list')
    login_url = '/login/'

    def get_object(self):
        return get_object_or_404(InventoryModel, pk=self.kwargs['pk'])

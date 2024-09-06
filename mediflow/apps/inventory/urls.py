from django.urls import path
from .views import InventoryListView, InventoryCreateView, InventoryUpdateView

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('update/<int:pk>/', InventoryUpdateView.as_view(), name='inventory-update'),
]

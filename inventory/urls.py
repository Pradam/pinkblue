from django.urls import path
from .views import Index, InventoryList

urlpatterns = [
    path('dashboard/', Index.as_view(), name="index"),
    path('get/inventory/data/', InventoryList.as_view(), name="list-inventory")
]

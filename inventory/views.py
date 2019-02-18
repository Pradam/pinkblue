from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
# Create your views here.

class Index(TemplateView):
    template_name = "index.html"


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.filter(active=2)
    serializer_class = InventorySerializer

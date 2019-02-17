from django.urls import path
from .views import Index

urlpatterns = [
    path('dashboard/', Index.as_view(), name="index"),
]

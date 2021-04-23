"""Django urlpatterns declaration for nautobatfishbot plugin."""
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('nautobatfishbot/', views.nautobatfishbot, name="nautobatfishbot_homepage")
]

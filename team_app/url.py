from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('fines/', views.fines),
]
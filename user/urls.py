from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('add_atc/', views.add_atc, name='add_atc'),
    path('add_runway/', views.add_runway, name='add_runway'),
    path('add_near/', views.add_near, name='add_near'),
    path('add_path/', views.add_path, name='add_path'),
    path('add_flight/', views.add_flight, name='add_flight'),
]

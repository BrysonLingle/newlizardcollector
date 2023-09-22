from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('about/', views.about, name='about'),
    path('all_lizard/', views.all_lizards, name='all_lizard'),
    path('', views.home, name='home'),  
]

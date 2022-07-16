from django.contrib import admin
from django.urls import path, include
from backend_api import views

urlpatterns = [
    path('', views.index, name=''),
    path('html/', views.html, name='html'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]

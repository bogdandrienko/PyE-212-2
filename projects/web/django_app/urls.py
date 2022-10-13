from django.contrib import admin
from django.urls import path, include
from django_app import views

# app = "django_app"
urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name='home'),

    path('index/', views.HomeView.as_view(), name='index'),
]

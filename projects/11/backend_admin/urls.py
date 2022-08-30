from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from backend_admin import views


urlpatterns = [
    path('', views.index),
]

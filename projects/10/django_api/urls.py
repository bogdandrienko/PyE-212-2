from django.urls import path
from django_api import views

urlpatterns = [
    path('', views.index, name=''),
]

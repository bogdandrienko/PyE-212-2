from django.urls import path
from django_api import views

urlpatterns = [
    path('', views.index, name=''),

    path('get_users/', views.get_users, name='get_users'),
]

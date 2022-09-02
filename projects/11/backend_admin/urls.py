from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from backend_admin import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='HomeView'),

    re_path(r'^get_active_user_list/$', views.GetActiveUserListView.as_view(), name='get_active_user_list'),
    re_path(r'^login/$', views.django_login, name='login'),
    re_path(r'^logout/$', views.django_logout, name='logout'),
]

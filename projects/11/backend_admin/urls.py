from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from backend_admin import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='HomeView'),

    re_path(r'^get_active_user_list1/$', views.GetActiveUserListView.as_view(), name='get_active_user_list1'),
    re_path(r'^get_active_user_list/$', views.get_active_user_list, name='get_active_user_list'),
    re_path(r'^login/$', views.django_login, name='login'),
    re_path(r'^logout/$', views.django_logout, name='logout'),

    re_path(r'^receipt/(?P<receipt_id>\d+)/$', views.receipt, name='receipt_id'),  # GET(one) / PUT (PUTCH) / DELETE
    re_path(r'^receipt/$', views.receipt, name='receipt'),  # GET(all) / POST
]

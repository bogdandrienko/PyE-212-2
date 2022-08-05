from django.contrib import admin
from django.urls import path, include, re_path
from backend_api import views

urlpatterns = [
    path('', views.index, name=''),
    
    path('login/', views.login, name='login'),
    

    #
    re_path(r'^news/(?P<book_id>\d+)/$', views.news),
    re_path(r'^news/$', views.news),

    re_path(r'^categories/$', views.categories),
    
    
    
    
    path('html/', views.html, name='html'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]

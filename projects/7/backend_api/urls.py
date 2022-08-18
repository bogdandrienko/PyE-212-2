from django.contrib import admin
from django.urls import path, include, re_path
from backend_api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name=''),
    
    path('login/', views.login, name='login'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #
    re_path(r'^news/(?P<book_id>\d+)/$', views.news),
    re_path(r'^news/$', views.news),

    re_path(r'^categories/(?P<category_id>\d+)/$', views.categories),
    re_path(r'^categories/$', views.categories),


    re_path(r'^get_data/$', views.get_public_books, name='get_data'),



    re_path(r'^top/$', views.top),

    re_path(r'^book/(?P<book_id>\d+)/$', views.book),


    path('html/', views.html, name='html'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]

from django.urls import path, re_path
from django_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django_app.views import MyPostViewSet#для класов
from django.contrib.auth import views as auth_views
#

from django.shortcuts import redirect
urlpatterns = [
    path('', views.index, name="index"),

    path('frontpage/',views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='django_app/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('registration/', views.registration, name='registration' ),

    re_path(route=r'profile/(?P<profile_id>\d+)/$', view= views.profile),
    path('profile/', views.profile, name='profile'),

    path('users/', views.users, name='users'),

    path('video/', views.videos, name='videos'),
    
    # re_path(route=r'^users/(?P<user_id>\d+)/$', view=views.users, ),
    

    path('profilephoto/', views.MyProfilePhoto.as_view()),

   
    path('mypost/', views.MyPostViewSet.as_view()),

    path('parsingexchange/', views.parsing_exchange, name='parsing_exchange'),

    re_path(r'^.*$', lambda request: redirect('/', permanent=False), name='redirect'),
    
]



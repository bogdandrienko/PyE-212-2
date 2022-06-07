from django.urls import path
from app_teacher.views import login, home, register

urlpatterns = [
    path(route='', view=home, name=""),
    path(route='home/', view=home, name="home"),

    path(route='login/', view=login, name="login"),
    path(route='register/', view=register, name="register"),
]

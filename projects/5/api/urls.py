from django.urls import path
from api import views


urlpatterns = [
    path(route='', view=views.home, name=""),
]

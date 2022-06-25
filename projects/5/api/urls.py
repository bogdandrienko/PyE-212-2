from django.urls import path
from api import views


urlpatterns = [
    path(route='', view=views.home, name=""),

    path(route='api/get_users/', view=views.get_users),
    path(route='api/get_users_count/', view=views.get_users_count),
    path(route='api/create_user/', view=views.create_user),
]

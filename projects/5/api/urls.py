from django.urls import path
from api import views


urlpatterns = [
    path(route='', view=views.home, name=""),

    path(route='api/get_users/', view=views.get_users),
    path(route='api/get_users_count/', view=views.get_users_count),
    path(route='api/create_user/', view=views.create_user),
    path(route='api/check_user/', view=views.check_user),
    path(route='api/login_user/', view=views.login_user),
    
    path(route='api/chat/create/', view=views.chat_create),  # POST - request - создание сообщения
    path(route='api/chat/read/', view=views.chat_read),  # GET - request - чтений сообщений
    path(route='api/chat/read/<int:sms_id>/', view=views.chat_read_id),  # GET - request - чтений сообщения по id
    
    # REST api ~ CRUD
]

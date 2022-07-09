from django.urls import path, re_path
from api import views


urlpatterns = [
    path(route='', view=views.home, name=""),

    path(route='api/get_users/', view=views.get_users),
    path(route='api/get_users_count/', view=views.get_users_count),
    path(route='api/create_user/', view=views.create_user),
    path(route='api/check_user/', view=views.check_user),
    path(route='api/login_user/', view=views.login_user),

    # CRUD
    path(route='api/chat/create/', view=views.chat_create),  # POST - request - создание сообщения
    path(route='api/chat/read/', view=views.chat_read),  # GET - request - чтений сообщений
    path(route='api/chat/read/<int:sms_id>/', view=views.chat_read_id),  # GET - request - чтений сообщения по id
    path(route='api/chat/delete/<int:sms_id>/', view=views.chat_delete_id),  # DELETE - request - удаление сообщения по id

    
    # REST api ~ CRUD

    # ^todos/$
    # "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    # ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@!%&*?])[A-Za-z\d#$@!%&*?]{8,30}$

    # READ(all) - get | CREATE - post
    re_path(route=r'^api/todo/$', view=views.todo),

    # READ - get | DELETE - delete | UPDATE - put (post)
    re_path(route=r'^api/todo/(?P<todo_id>\d+)/$', view=views.todo_by_id),
]

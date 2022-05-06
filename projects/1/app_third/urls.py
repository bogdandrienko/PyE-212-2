from django.urls import path
from .views import home, index, about, login

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', home),
    path('home/', home),
    path('login/', login),
    path('index/', index),
    path('about/', about),

    # path('todo_create/', idea_create, name='django_idea_create'),
    # path('todo_detail/<int:todo_id>/', idea_change, name='django_idea_change'),
    # path('todo_list/', idea_list, name='django_idea_list'),
]

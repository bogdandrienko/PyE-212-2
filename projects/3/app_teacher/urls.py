from django.urls import path
from .views import home, index, about, login, todo_detail
from . import views as logic

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', home, ""),
    path('home/', home, name="home"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),

    path('todo_detail/<int:todo_id>/', todo_detail, name="todo_detail"),
    path(route='todo_list/', view=logic.todo_list, name="todo_list"),
    path(route='todo_create/', view=logic.todo_create, name="todo_create"),
]

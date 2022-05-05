from django.urls import path
from .views import home, index, about, login

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', home),
    path('home/', home),
    path('login/', login),
    path('index/', index),
    path('about/', about),
]

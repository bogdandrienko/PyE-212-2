from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_second import views

# прямой импорт
import django

# импорт с псевдонимом
# import urllib3 as lib

# относительный импорт
# from .asgi

from app_second import urls

# Определяет ВСЮ маршрутизацию (пути в адресной строке браузера)

urlpatterns = [
    # Подключаем "административные" функции Django
    path('admin/', admin.site.urls),

    # "Добавляет" пути в общий путь маршрутизации, которые лежат в 'app_second.urls'
    path('', include('app_second.urls')),
    # path('', views.home),
    # path('home/', views.home),
    # path('login/', views.login),
    # path('index/', views.index),
    # path('about/', views.about),
    path('origin_home/', views.origin_home),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

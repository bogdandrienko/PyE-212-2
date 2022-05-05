from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Определяет ВСЮ маршрутизацию (пути в адресной строке браузера)

urlpatterns = [
    # Подключаем "административные" функции Django
    path('admin/', admin.site.urls),

    # "Добавляет" пути в общий путь маршрутизации, которые лежат в 'app_second.urls'
    path('', include('app_second.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

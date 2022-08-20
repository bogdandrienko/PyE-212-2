from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_api import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS

    path('admin/', admin.site.urls),

    path('', views.index, name=''),

    path('api/', include('django_api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

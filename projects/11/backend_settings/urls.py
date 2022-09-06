from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from backend_api import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('moderator/', include('backend_admin.urls')),

    path('api/', include('backend_api.urls')),

    path('api/', include('rest_framework.urls')),
]


urlpatterns += [re_path(r'^.*$', lambda request: redirect('/', permanent=False), name='redirect')]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
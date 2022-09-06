from django.contrib import admin
from backend_admin import models


admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление приложением'
admin.site.site_title = 'Панель'

class LogAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Log' на панели администратора
    """

    list_display = (  # поля для отображения
        'path',
        'method',
        'user',
        'error',
        'created',
    )
    list_display_links = (  # поля-ссылка
        'path',
        'method',
        'user',
        'created',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'error',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'path',
        'method',
        'user',
        'error',
        'created',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'path',
            'method',
            'user',
            'error',
            'created',
        )}),
    )
    search_fields = [  # поле для поиска
        'path',
        'method',
        'user',
        'error',
        'created',
    ]


admin.site.register(models.Log, LogAdmin)
admin.site.register(models.Profile)
# admin.site.register(models.UserExtend)

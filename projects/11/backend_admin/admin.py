from django.contrib import admin

from backend_admin import models


# Register your models here.
class LogAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Log' на панели администратора
    """

    list_display = (  # поля для отображения
        'path',
        'user',
        'error',
        'created',
    )
    list_display_links = (  # поля-ссылка
        'path',
        'user',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'error',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'path',
        'user',
        'error',
        'created',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'path',
            'user',
            'error',
            'created',
        )}),
    )
    search_fields = [  # поле для поиска
        'path',
        'user',
        'error',
        'created',
    ]


admin.site.register(models.Log, LogAdmin)

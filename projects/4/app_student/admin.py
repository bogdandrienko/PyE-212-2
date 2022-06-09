from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Country)


class CityAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'City' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'country_id',
    )
    list_display_links = (  # поля-ссылка
        # 'title',
        # 'country_id',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'country_id',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
        # 'country_id',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'country_id',
        )}),
        ('Дополнительно', {'fields': (
            'title',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'country_id',
    ]


admin.site.register(models.City, CityAdmin)
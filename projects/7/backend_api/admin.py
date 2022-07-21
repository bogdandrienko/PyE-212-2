from django.contrib import admin
from backend_api.models import ModelBook, ModelBookCategory

# Register your models here.

admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление моделями!'
admin.site.site_title = 'Панель3'


class ModelBookAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Receipt' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'image',
        'description',
        'is_completed',
        'upload_author',
        'time_to_cook',
        'instructions',
    )
    # filter_horizontal = ('ingredients', 'category',)  # только для полей формата many_to_many_field
    list_display_links = (  # поля-ссылка
        'title',
        'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_completed',
        'upload_author',
        'time_to_cook',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'image',
        'description',
        'is_completed',
        'upload_author',
        'time_to_cook',
        'instructions',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
            'description',
            # 'ingredients',
        )}),
        ('Дополнительно', {'fields': (
            'image',
            'category',
            'time_to_cook',
            'instructions',
        )}),
        ('Вспомогательное', {'fields': (
            'is_completed',
            'upload_author',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'is_completed',
        'upload_author',
        'time_to_cook',
        'instructions',
    ]

class ModelBookCategoryAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptCategory' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
    )
    list_display_links = (  # поля-ссылка
        'title',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
    ]

admin.site.register(ModelBookCategory, ModelBookCategoryAdmin)
admin.site.register(ModelBook, ModelBookAdmin)
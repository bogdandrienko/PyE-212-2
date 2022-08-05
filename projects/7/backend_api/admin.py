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
        # 'description',
        'is_view',
        'upload_author',
        'time_to_read',
        'instructions',
    )
    # filter_horizontal = ('ingredients', 'category',)  # только для полей формата many_to_many_field
    list_display_links = (  # поля-ссылка
        'title',
        # 'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_view',
        'upload_author',
        'time_to_read',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'image',
        # 'description',
        'is_view',
        'upload_author',
        'time_to_read',
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
            'time_to_read',
            'instructions',
        )}),
        ('Вспомогательное', {'fields': (
            'is_view',
            'upload_author',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'is_view',
        'upload_author',
        'time_to_read',
        'instructions',
    ]


class ModelBookCategoryAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptCategory' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'description',
    )
    list_display_links = (  # поля-ссылка
        'title',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'description',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
        'description',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
            'description',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'description',
    ]


admin.site.register(ModelBookCategory, ModelBookCategoryAdmin)
admin.site.register(ModelBook, ModelBookAdmin)

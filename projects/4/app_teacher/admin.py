from django.contrib import admin
from app_teacher.models import Receipt, ReceiptCategory, ReceiptRating, ReceiptComment

# Register your models here.

admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление моделями!'
admin.site.site_title = 'Панель3'


class ReceiptAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Receipt' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'image',
        'description',
        'is_completed',
        'category',
    )
    list_display_links = (  # поля-ссылка
        'title',
        'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_completed',
        'category',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
        'image',
        'description',
        'is_completed',
        'category',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
            'description',
        )}),
        ('Дополнительно', {'fields': (
            'image',
            'category',
        )}),
        ('Вспомогательное', {'fields': (
            'is_completed',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'is_completed',
        'category',
    ]


class ReceiptCategoryAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Receipt' на панели администратора
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


admin.site.register(ReceiptCategory, ReceiptCategoryAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ReceiptRating)
admin.site.register(ReceiptComment)

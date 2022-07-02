from django.contrib import admin

from . import models
# Register your models here.


class ReceiptIngredientAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'name',
    )
    list_display_links = (  # поля-ссылка
        'name',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'name',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'name',
        )}),
    )
    search_fields = [  # поле для поиска
        'name',
    ]


admin.site.register(models.ReceiptIngredient, ReceiptIngredientAdmin)

class TextModelAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'TextModel' на панели администратора
    """

    list_display = (  # поля для отображения
        'text',
        'created_datetime',
    )
    list_display_links = (  # поля-ссылка
        'text',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'text',
        'created_datetime',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'text',
            'created_datetime',
        )}),
    )
    search_fields = [  # поле для поиска
        'text',
        'created_datetime',
    ]


admin.site.register(models.TextModel, TextModelAdmin)
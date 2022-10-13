from django.contrib import admin
from django_app import models

class CarAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
    )
    list_display_links = (  # поля-ссылка
        'title',
    )
    list_editable = (  # поля для редактирования объекта на лету
        # 'is_liked',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('EXTRA: ', {'fields': (
            'title',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
    ]

# Register your models here.
admin.site.register(models.Car, CarAdmin)

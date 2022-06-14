from django.contrib import admin
from app_teacher.models import Receipt, ReceiptCategory, ReceiptRating, ReceiptComment, ReceiptIngredient

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
        'author',
        'time_to_cook',
        'instructions',
    )
    filter_horizontal = ('ingredients', 'category',)  # только для полей формата many_to_many_field
    list_display_links = (  # поля-ссылка
        'title',
        'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_completed',
        'author',
        'time_to_cook',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'image',
        'description',
        'is_completed',
        'author',
        'time_to_cook',
        'instructions',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
            'description',
            'ingredients',
        )}),
        ('Дополнительно', {'fields': (
            'image',
            'category',
            'time_to_cook',
            'instructions',
        )}),
        ('Вспомогательное', {'fields': (
            'is_completed',
            'author',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'is_completed',
        'author',
        'time_to_cook',
        'instructions',
    ]


class ReceiptCategoryAdmin(admin.ModelAdmin):
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


class ReceiptCommentAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'comment_text',
        'user',
        'receipt',
        'time',
    )
    list_display_links = (  # поля-ссылка
        'comment_text',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'comment_text',
        'user',
        'receipt',
        'time',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'comment_text',
            'user',
            'receipt',
            'time',
        )}),
    )
    search_fields = [  # поле для поиска
        'comment_text',
        'user',
        'receipt',
        'time',
    ]


class ReceiptRatingAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptIngredient' на панели администратора
    """

    list_display = (  # поля для отображения
        'is_liked',
        'rating_value',
        'user',
        'receipt',
    )
    list_display_links = (  # поля-ссылка
        'is_liked',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_liked',
    )
    list_filter = (  # поля для редактирования объекта на лету
        'is_liked',
        'rating_value',
        'user',
        'receipt',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'is_liked',
            'rating_value',
            'user',
            'receipt',
        )}),
    )
    search_fields = [  # поле для поиска
        'is_liked',
        'rating_value',
        'user',
        'receipt',
    ]


admin.site.register(ReceiptCategory, ReceiptCategoryAdmin)
admin.site.register(ReceiptIngredient, ReceiptIngredientAdmin)
# admin.site.register(ReceiptIngredient)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ReceiptRating)
admin.site.register(ReceiptComment, ReceiptCommentAdmin)

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class ReceiptCategory(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=250,
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории рецептов'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.title}'


class ReceiptIngredient(models.Model):
    name = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Название",
        verbose_name="Название:",
        help_text='<small class="text-muted">это наше название</small><hr><br>',
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.name}'


class Receipt(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=250,
    )
    image = models.ImageField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="img/receipt/default/default_receipt.jpg",
        verbose_name="Заставка:",
        help_text='<small class="text-muted">это наша заставка</small><hr><br>',

        validators=[FileExtensionValidator(['jpg', 'png'])],
        upload_to='img/receipt',
        max_length=100,
    )
    time_to_cook = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="1",
        verbose_name="Время на приготовление(минуты)",
        help_text='<small class="text-muted">это наше время на приготовление</small><hr><br>',

        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )
    category = models.ManyToManyField(
        db_column='country_db_column',
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='Категория блюда',
        help_text='<small class="text-muted">категория</small><hr><br>',

        to=ReceiptCategory,
    )
    author = models.ForeignKey(
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор блюда',
        help_text='<small class="text-muted">автор</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE - удаляет всю запись, при удалении связанной записи
        # SET_NULL - зануляет всю запись, при удалении связанной записи DO_NOTHING - ничего не делать
    )
    ingredients = models.ManyToManyField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='Ингредиенты блюда',
        help_text='<small class="text-muted">ингредиенты</small><hr><br>',

        to=ReceiptIngredient,
    )

    description = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=False,
        null=False,
        default="Описание",
        verbose_name="Описание:",
        help_text='<small class="text-muted">это наше Описание</small><hr><br>',
    )
    is_completed = models.BooleanField(
        default=False,
        # editable=
    )
    instructions = models.FileField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Инструкция:",
        help_text='<small class="text-muted">Инструкция</small><hr><br>',

        validators=[FileExtensionValidator(['PDF', 'XLSX'])],

        upload_to='file/pdf',
        max_length=100,
    )

    # is_show = models.BooleanField(
    #     default=False,
    #     # editable=
    # )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title', 'description')
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):  # возвращает строковое представление объекта
        return f'{self.title}'

    def return_clear_data(self):
        title = self.title
        return str(title).strip() + " banana"

    def get_rating(self):
        ratings = ReceiptRating.objects.filter(
            receipt=Receipt.objects.get(id=self.id),
        )

        like_count = 0
        dislike_count = 0
        for rating in ratings:
            if rating.is_liked:
                like_count += 1
            else:
                dislike_count += 1

        return dict(total=ratings.count, like_count=like_count, dislike_count=dislike_count)


class ReceiptComment(models.Model):
    comment_text = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Текст комментария",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">Текст комментария</small><hr><br>',

        max_length=500,
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">Пользователь</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE SET_NULL DO_NOTHING
    )
    receipt = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Рецепт',
        help_text='<small class="text-muted">Рецепт</small><hr><br>',

        to=Receipt,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )
    time = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name="время создания:",
        help_text='<small class="text-muted">время создания</small><hr><br>',

        auto_now_add=False,
        auto_now=False,
    )
    create = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        # default=timezone.now,
        verbose_name="время создания:",
        help_text='<small class="text-muted">время создания</small><hr><br>',

        auto_now_add=True,  # автоматически добавляет время в момент создания объекта (нельзя редактировать)
        auto_now=False,  # автоматически добавляет время в момент создания и изменения объекта (нельзя редактировать)
    )
    update = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        # default=timezone.now,
        verbose_name="время создания:",
        help_text='<small class="text-muted">время создания</small><hr><br>',

        auto_now_add=False,  # автоматически добавляет время в момент создания объекта (нельзя редактировать)
        auto_now=True,  # автоматически добавляет время в момент создания и изменения объекта (нельзя редактировать)
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('-time',)
        verbose_name = 'Комментарий к рецепту'
        verbose_name_plural = 'Комментарии к рецептам'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.comment_text[:10:1]}'


# сигнал на обновление времени в комментарии
@receiver(post_save, sender=ReceiptComment)
def update_comment_time(sender, instance, created, **kwargs):
    if not created:  # если объект не создан впервые
        obj = ReceiptComment.objects.get(id=instance.id)
        if obj.time != timezone.now():
            obj.time = timezone.now()
            obj.save()


class ReceiptRating(models.Model):
    is_liked = models.BooleanField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=False,
        verbose_name="Лайк:",
        help_text='<small class="text-muted">Лайк</small><hr><br>',
    )
    rating_value = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="0",
        verbose_name="Оценка",
        help_text='<small class="text-muted">Оценка</small><hr><br>',

        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">Пользователь</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )
    receipt = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Рецепт',
        help_text='<small class="text-muted">Рецепт</small><hr><br>',

        to=Receipt,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('receipt',)
        verbose_name = 'Рейтинг рецепта'
        verbose_name_plural = 'Рейтинги рецептов'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.receipt}'

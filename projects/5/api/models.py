from django.db import models
from django.utils import timezone


# Create your models here.


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
        app_label = 'api'
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.name}'


class TextModel(models.Model):
    text = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="текст сообщения:",
        help_text='<small class="text-muted">это наше сообщение</small><hr><br>',

        max_length=500,
    )
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="проверка сообщения:",
        help_text='<small class="text-muted">это наше сообщение</small><hr><br>',

        max_length=500,
    )
    created_datetime = models.DateTimeField(
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

    class Meta:
        app_label = 'api'
        ordering = ('text',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.text[:30:1]}'

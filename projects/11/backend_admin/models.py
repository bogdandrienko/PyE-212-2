from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Log(models.Model):
    path = models.URLField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Маршрут",
        help_text='<small class="text-muted">Маршрут</small><hr><br>',

        max_length=128,
    )
    user = models.ForeignKey(
        primary_key=False,
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
    error = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="нет ошибки",
        verbose_name="Ошибка:",
        help_text='<small class="text-muted">Ошибка или текст исключения</small><hr><br>',

        max_length=512,
    )
    created = models.DateTimeField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">datetime_field</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'auth'
        ordering = ('-created', 'user')
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

    def __str__(self):
        return f'{self.created} {self.path[:30]} {self.user.username[:30]}'

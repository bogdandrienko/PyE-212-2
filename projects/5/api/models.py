from django.db import models

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

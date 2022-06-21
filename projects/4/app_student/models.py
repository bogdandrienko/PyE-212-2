from django.db import models


# Create your models here.


class Country(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="Имя страны",
        verbose_name="Имя страны:",
        help_text='<small class="text-muted">Имя страны</small><hr><br>',

        max_length=254,
    )

    def __str__(self):
        return f'{self.title}'


class City(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="Имя города",
        verbose_name="Имя города:",
        help_text='<small class="text-muted">Имя страны</small><hr><br>',

        max_length=254,
    )
    country_id = models.ForeignKey(
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
        null=True,
        default=None,
        verbose_name='Из какой страны',
        help_text='<small class="text-muted">Из какой страны</small><hr><br>',

        to=Country,
        on_delete=models.SET_NULL,  # CASCADE SET_NULL DO_NOTHING
    )

    def __str__(self):
        return f'{self.title} ({self.country_id})'

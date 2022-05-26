from django.db import models
from app_student.models import Country

# Create your models here.


class Task(models.Model):
    """
    Класс с данными по нашей задаче
    """

    # id = AutoIncrement

    # Символьный тип данных (<= 500 символов)
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=254,
    )
    description = models.TextField(
        unique=False,
        # editable=
    )
    is_completed = models.BooleanField(
        default=False,
        # editable=
    )

    def return_clear_data(self):
        title = self.title
        return str(title).strip() + " banana"

    # One to one
    # One to many
    # Many to manu

    # title = models.

# class City(models.Model):
#     title = models.CharField(
#         primary_key=False,
#         unique=True,
#         editable=True,
#         blank=True,
#         null=False,
#         default="Имя города",
#         verbose_name="Имя города:",
#         help_text='<small class="text-muted">Имя страны</small><hr><br>',
#
#         max_length=254,
#     )
#     country = models.ForeignKey(
#         db_column='country_db_column',
#         db_index=True,
#         db_tablespace='country_db_tablespace',
#         error_messages=False,
#         primary_key=False,
#         unique_for_date=False,
#         unique_for_month=False,
#         unique_for_year=False,
#         unique=False,
#         editable=True,
#         blank=True,
#         null=True,
#         default=None,
#         verbose_name='Из какой страны',
#         help_text='<small class="text-muted">Из какой страны</small><hr><br>',
#
#         to=Country,
#         on_delete=models.SET_NULL,  # CASCADE SET_NULL DO_NOTHING
#     )
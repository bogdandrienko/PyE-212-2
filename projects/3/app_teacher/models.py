from django.db import models


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

    # title = models.

from django.db import models


# Create your models here.

class Task(models.Model):
    """
    Класс с данными по нашей задаче
    """

    # скрыт из коробки
    # id = models.BigAutoField

    # Символьный тип данных (<= 254 символов)
    title = models.CharField(
        unique=False,
        max_length=254,
        # editable=
        # default=""
    )
    # Текстовый тип данных (большой объём)
    description = models.TextField(
        unique=False,
        # editable=
    )


    # title = models.
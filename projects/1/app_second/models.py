from django.db import models


# Create your models here.

class Task(models.Model):
    """
    Класс с данными по нашей задаче
    """

    # Символьный тип данных (<= 500 символов)
    title = models.CharField(
        unique=False,
        max_length=254,
        # editable=
    )

    # title = models.
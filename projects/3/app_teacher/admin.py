from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Task)  # отображение модели Task в админке

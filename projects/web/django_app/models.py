from django.db import models


# Create your models here.

class Car(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Model",
        verbose_name="Model:",
        help_text='<small class="text-muted">это Model</small><hr><br>',

        max_length=120,
    )

    class Meta:
        app_label = "django_app"
        ordering = ('-title',)
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.title[:10]}..."

    def get_cars_count(self):
        count = Car.objects.all().count()
        return count

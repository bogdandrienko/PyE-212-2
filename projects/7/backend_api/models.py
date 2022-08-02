from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class ModelBookCategory(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="Название категории",
        verbose_name="Название категории:",
        help_text='<small class="text-muted">это наше название</small><hr><br>',

        max_length=200,
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории книг'

    def __str__(self):
        return f'{self.title}'


class ModelBook(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=250,
    )
    image = models.ImageField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="default/modelbooks/default_book.jpg",
        verbose_name="Заставка:",
        help_text='<small class="text-muted">это наша заставка</small><hr><br>',

        validators=[FileExtensionValidator(['jpg', 'png', 'bmp', 'jpeg'])],
        upload_to='modelbooks',  # /static/ media/ modelbooks/ image.jpg
        max_length=100,
    )
    time_to_cook = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="1",
        verbose_name="Время на приготовление(минуты)",
        help_text='<small class="text-muted">это наше время на приготовление</small><hr><br>',

        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )
    category = models.ManyToManyField(
        db_column='country_db_column',
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='Категория блюда',
        help_text='<small class="text-muted">категория</small><hr><br>',

        to=ModelBookCategory,
    )
    upload_author = models.ForeignKey(
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Кто загрузил',
        help_text='<small class="text-muted">автор</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE - удаляет всю запись, при удалении связанной записи
        # SET_NULL - зануляет всю запись, при удалении связанной записи DO_NOTHING - ничего не делать
    )
    description = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=False,
        null=False,
        default="Описание",
        verbose_name="Описание:",
        help_text='<small class="text-muted">это наше Описание</small><hr><br>',
    )
    is_completed = models.BooleanField(
        default=False,
        # editable=
    )
    instructions = models.FileField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Инструкция:",
        help_text='<small class="text-muted">Инструкция</small><hr><br>',

        validators=[FileExtensionValidator(['PDF', 'XLSX'])],

        upload_to='file/pdf',
        max_length=100,
    )

    # is_show = models.BooleanField(
    #     default=False,
    #     # editable=
    # )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title', 'description')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):  # возвращает строковое представление объекта
        return f'{self.title}'

    def return_clear_data(self):
        title = self.title
        return str(title).strip() + " banana"

    # def get_rating(self):
    #     ratings = ReceiptRating.objects.filter(
    #         receipt=Receipt.objects.get(id=self.id),
    #     )

    #     like_count = 0
    #     dislike_count = 0
    #     for rating in ratings:
    #         if rating.is_liked:
    #             like_count += 1
    #         else:
    #             dislike_count += 1

    #     return dict(total=ratings.count, like_count=like_count, dislike_count=dislike_count)

from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class ModelBookCategory(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="Название категории",
        verbose_name="Название категории:",
        help_text='<small class="text-muted"></small><hr><br>',

        max_length=200,
    )
    description = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=False,
        null=False,
        default="Описание",
        verbose_name="Описание:",
        help_text='<small class="text-muted"></small><hr><br>',
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class ModelBook(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted"></small><hr><br>',

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

        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])],
        upload_to='modelbooks/avatar',  # /static/ media/ modelbooks/ image.jpg
        max_length=100,
    )
    time_to_read = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="1",
        verbose_name="Время на чтение",
        help_text='<small class="text-muted"></small><hr><br>',

        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )
    category = models.ManyToManyField(
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='Категория',
        help_text='<small class="text-muted"></small><hr><br>',

        to=ModelBookCategory,
    )
    upload_author = models.ForeignKey(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор загрузил',
        help_text='<small class="text-muted"></small><hr><br>',

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
    is_view = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name="Видимость книги в общем доступе:",
        help_text='<small class="text-muted"></small><hr><br>',
    )
    instructions = models.FileField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Инструкция:",
        help_text='<small class="text-muted">Инструкция</small><hr><br>',

        validators=[FileExtensionValidator(['PDF'])],

        upload_to='modelbooks/file',
        max_length=100,
    )
    created_datetime_field = models.DateTimeField(
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
    update_datetime_field = models.DateTimeField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время обновления',
        help_text='<small class="text-muted">datetime_field</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

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


class Profile(models.Model):
    user = models.ForeignKey(
        primary_key=True,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default=None,
        verbose_name='Аккаунт',
        help_text='<small class="text-muted">Аккаунт</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(
        unique=False,
        editable=True,
        blank=False,
        null=True,
        default="",
        verbose_name="Биография:",
        help_text='<small class="text-muted">это наша Биография</small><hr><br>',
    )

    # mobile = None
    # avatar = None
    # isBanned = None
    # email = None
    # rassilka = None

    class Meta:
        app_label = 'auth'
        ordering = ('user',)
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'профиль: {self.user.username} {self.bio[:20]}...'


class Profile2(models.Model):
    user = models.OneToOneField(
        primary_key=True,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default=None,
        verbose_name='Аккаунт',
        help_text='<small class="text-muted">Аккаунт</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(
        unique=False,
        editable=True,
        blank=False,
        null=True,
        default="",
        verbose_name="Биография:",
        help_text='<small class="text-muted">это наша Биография</small><hr><br>',
    )

    # mobile = None
    # avatar = None
    # isBanned = None
    # email = None
    # rassilka = None

    class Meta:
        app_label = 'auth'
        ordering = ('user',)
        verbose_name = 'Профиль пользователя 2'
        verbose_name_plural = 'Профили пользователей 2'

    def __str__(self):
        return f'профиль: {self.user.username} {self.bio[:20]}...'


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    if created:
        # тут происходит первое создание модели
        Profile.objects.get_or_create(user=instance)
        Profile2.objects.get_or_create(user=instance)
    else:
        # тут происходит каждое сохранение модели
        Profile.objects.get_or_create(user=instance)
        Profile2.objects.get_or_create(user=instance)

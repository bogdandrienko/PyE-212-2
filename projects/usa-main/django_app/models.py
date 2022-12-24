from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save
#



#категория историй
class StoryCategory(models.Model): 
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        
        #default="Заголовок категории истории",
        verbose_name="Заголовок категории истории",
        help_text='<small class="text-muted">это наш заголовок категории истории</small><hr><br>',
        max_length=250,
    )

    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'Категории историй'    
        verbose_name_plural = 'Категории историй'

    def __str__(self) -> str:
        return f'{self.title}'



# для картинок
def upload_to (instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyPost(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listings")

    title = models.CharField(
        max_length=80, blank=False, null=True)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'посты'    
        verbose_name_plural = 'посты'

    def __str__(self) -> str:
        return f'{self.title}'




# для картинок
# def upload_to_avatar (instance, filename):
#     return 'avatars/{filename}'.format(filename=filename)

def upload_to_avatar (instance, filename):
    return '/'.join(['avatars', filename])

class Profile(models.Model):
    user = models.OneToOneField(
        primary_key=True,
        editable=True,
        blank=True,
        null=False,
        default=None,
        verbose_name='Аккаунт',

        to=User,
        on_delete=models.CASCADE,
    )

    avatar = models.ImageField(
        null=True,       
        blank=True,       
        upload_to=upload_to_avatar,
        default='avatars/ava.jpg'
    )    

    class Meta:
        app_label = 'auth'
        ordering =('user',)
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
    
    def __str__(self):
        return f'профиль: {self.user.username}'


#сигнал при создании юзера автоматом создаст таблицу profile 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # тут происходит первое создание модели
        Profile.objects.get_or_create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)


class youtube_video_category(models.Model): 
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        
        #default="Заголовок категории истории",
        verbose_name="Заголовок категории видео",
        help_text='<small class="text-muted">это наш заголовок категории видео</small><hr><br>',
        max_length=250,
    )

    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'Категории видео'    
        verbose_name_plural = 'Категории видео'

    def __str__(self) -> str:
        return f'{self.title}'

class youtube_video(models.Model):
    creator = models.ForeignKey(
        null=True,
        blank=True,
        to=User, 
        on_delete=models.SET_NULL)

    title = models.CharField(
        max_length=256,
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым      
    )    

    description = models.TextField(        
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым       
        default="Описание",
        verbose_name="Описание",        
    )

    category_id = models.ManyToManyField(
        blank=True,  
        verbose_name="Категория видео",
        to=youtube_video_category,
    )

    url_from_youtube = models.TextField(
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым 
    )

    datetime_field = models.DateTimeField(       
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
        # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'видео с ютуба'    
        verbose_name_plural = 'Ютуб видео'

    def __str__(self) -> str:
        return f'{self.title}'
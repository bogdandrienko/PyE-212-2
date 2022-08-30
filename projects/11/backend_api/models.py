from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

#
# class UserManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **kwargs):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)
#
#
# class UserExtend(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField('email address', unique=True)
#     first_name = models.CharField('first name', max_length=30, blank=True)
#     last_name = models.CharField('last name', max_length=30, blank=True)
#
#     user_email_spam_success = models.BooleanField('spam email', default=False)
#     phone = models.IntegerField('mobile phone', default=0)
#
#     date_joined = models.DateTimeField('date joined', auto_now_add=True)
#     is_active = models.BooleanField('active', default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#
#     is_staff = models.BooleanField('if user is moderator', default=True)
#     # is_superuser = models.BooleanField('if user is superuser', default=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         app_label = 'backend_api'
#         ordering = ('-date_joined',)
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#
#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         """
#         Returns the short name for the user.
#         """
#         return self.first_name


class Profile(models.Model):
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
    email = models.EmailField(
        unique=True,
        editable=True,
        blank=False,
        null=False,
        default="",
        verbose_name="Почта",
        help_text='<small class="text-muted">пример: bogdandrienko@gmail.com</small><hr><br>',
    )

    user_email_spam_success = models.BooleanField('spam email', default=False)
    phone = models.IntegerField('mobile phone', default=0)

    class Meta:
        app_label = 'auth'
        ordering = ('user',)
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'профиль: {self.user.username}...'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance, email=instance.username)
    else:
        Profile.objects.get_or_create(user=instance, email=instance.username)

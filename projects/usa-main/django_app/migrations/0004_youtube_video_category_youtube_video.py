# Generated by Django 4.1.2 on 2022-12-04 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0003_alter_mypost_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='youtube_video_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='<small class="text-muted">это наш заголовок категории видео</small><hr><br>', max_length=250, verbose_name='Заголовок категории видео')),
            ],
            options={
                'verbose_name': 'Категории видео',
                'verbose_name_plural': 'Категории видео',
            },
        ),
        migrations.CreateModel(
            name='youtube_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True, default='Описание', verbose_name='Описание')),
                ('url_from_youtube', models.TextField(blank=True)),
                ('datetime_field', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ManyToManyField(blank=True, to='django_app.youtube_video_category', verbose_name='Категория мороженого')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

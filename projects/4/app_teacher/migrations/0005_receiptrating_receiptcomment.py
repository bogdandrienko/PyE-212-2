# Generated by Django 4.0.4 on 2022-06-04 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0004_alter_receipt_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=250, null=True, verbose_name='Заголовок:')),
                ('receipt', models.ForeignKey(blank=True, db_column='country_db_column', db_tablespace='country_db_tablespace', default=None, error_messages=False, help_text='<small class="text-muted">категория</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_teacher.receipt', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Категория блюда')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории рецептов',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=250, null=True, verbose_name='Заголовок:')),
                ('receipt', models.ForeignKey(blank=True, db_column='country_db_column', db_tablespace='country_db_tablespace', default=None, error_messages=False, help_text='<small class="text-muted">категория</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_teacher.receipt', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Категория блюда')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории рецептов',
                'ordering': ('title',),
            },
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-07 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0009_alter_receiptingredient_options_receipt_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='category',
            field=models.ForeignKey(blank=True, db_column='country_db_column', db_tablespace='country_db_tablespace', default=None, error_messages=False, help_text='<small class="text-muted">категория</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_teacher.receiptcategory', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Категория блюда'),
        ),
    ]
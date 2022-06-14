# Generated by Django 4.0.4 on 2022-06-14 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0021_receiptcomment_time_alter_receiptrating_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptcomment',
            name='create',
            field=models.DateTimeField(auto_now_add=True, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:'),
        ),
        migrations.AddField(
            model_name='receiptcomment',
            name='update',
            field=models.DateTimeField(auto_now=True, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:'),
        ),
        migrations.AlterField(
            model_name='receiptcomment',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:'),
        ),
    ]
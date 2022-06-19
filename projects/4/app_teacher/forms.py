import datetime

from django import forms
from django.contrib.auth.models import User
from . import models


class ReceiptCreateForm(forms.Form):
    title = forms.CharField(
        disabled=False,  # Отключено ли поле в форме
        localize=False,  # Локализовать ли контент принудительно
        required=False,  # Требовать ли наличие данных в поле
        label='Заголовок',  # Заголовок поля
        help_text='<small class="text-muted underline">text</small><br>',  # Вспомогательный текст
        # для поля (Можно передавать html теги)
        initial='',  # Начальное значение поля (Имеет приоритет перед "widget.attrs.value")
        widget=forms.TextInput(
            attrs={
                'type': 'text',  # HTML тип поля
                'name': 'text',  # HTML имя поля
                'required': '',  # Требовать ли наличие данных в поле
                'placeholder': 'введите заголовок тут',  # Данные, которые видны при удалении всей информации
                'value': '',  # Начальное значение поля (Второстепенное по приориту после "initial")
                'class': 'form-control w-50 p-1 m-1',  # HTML / css / bootstrap классы

                'minlength': '3',
                'maxlength': '100',
            }
        ),
    )
    descriptions = forms.IntegerField(required=False)
    file = forms.FileField(required=False)
    image = forms.ImageField(required=False)
    date = forms.DateTimeField(required=False)
    datetime_ = forms.DateTimeField(
        disabled=False,  # Отключено ли поле в форме
        localize=False,  # Локализовать ли контент принудительно
        required=False,  # Требовать ли наличие данных в поле
        label='datetime',  # Заголовок поля
        help_text='<small class="text-muted underline">2021-11-18T10:27</small><br>',  # Вспомогательный текст
        # для поля (Можно передавать html теги)
        initial=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),  # Начальное значение поля (Имеет приоритет
        # перед "widget.attrs.value")
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',  # HTML тип поля
                'name': 'datetime',  # HTML имя поля
                'required': '',  # Требовать ли наличие данных в поле
                'placeholder': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),  # Данные, которые видны при
                # удалении всей информации
                'value': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),  # Начальное значение поля (
                # Второстепенное по приориту после "initial")
                'class': 'form-control w-25',  # HTML / css / bootstrap классы

                'min': "2021-07-30T01:00",
                'max': "2023-12-31T22:59",
                'format': '%Y-%m-%dT%H:%M:%S',
            }
        ),
    )
    body = forms.CharField(widget=forms.Textarea(attrs={'name': 'body', 'rows': '3', 'cols': '5'}), required=False)
    cc_myself = forms.BooleanField(required=False)


class ReceiptCreateForm2(forms.ModelForm):
    class Meta:
        model = models.Receipt
        fields = '__all__'


class ReceiptCommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.ReceiptComment
        fields = '__all__'
        # fields = ["username", "password", "email"]


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["username", "password", "email"]

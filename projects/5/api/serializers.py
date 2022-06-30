from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):  # сериализатор(конвертер данные в JSON)

    class Meta:
        model = User
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):  # сериализатор(конвертер данные из объекта модели в JSON)

    class Meta:
        model = models.ReceiptIngredient
        fields = '__all__'


class TextModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextModel
        fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):  # сериализатор(конвертер данные в JSON)

    class Meta:
        model = User
        fields = '__all__'

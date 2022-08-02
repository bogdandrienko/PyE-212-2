from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelBook
        fields = '__all__'

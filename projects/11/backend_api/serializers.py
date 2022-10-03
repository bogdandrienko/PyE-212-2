from django.contrib.auth.models import User
from rest_framework import serializers
from backend_api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ['room_number', 'date']


class ReceiptCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReceiptCategory
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Receipt
        fields = ['id', 'title', 'author']
        # fields = '__all__'

    # def get_category(self, obj) -> list:
    #     print(self)
    #     print(type(self))
    #
    #     print(obj)
    #     print(type(obj))



        # categories = models.Receipt.objects.all()
        # categories_serialized = serializers.ReceiptSerializer(instance=receipts, many=True).data
        #
        # ReceiptCategorySerializer

        # return []

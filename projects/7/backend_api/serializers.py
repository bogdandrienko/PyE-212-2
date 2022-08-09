from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_profile(self, obj):
        return ProfileSerializer(instance=models.Profile.objects.get(user=obj), many=False).data


class BookSerializer(serializers.ModelSerializer):
    apples = serializers.SerializerMethodField(read_only=True)
    upload_author1 = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    category2 = serializers.SerializerMethodField(read_only=True)

    profile2 = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.ModelBook
        fields = '__all__'

    def get_apples(self, obj):
        return {"apples": "1234124124"}

    def get_upload_author1(self, obj):
        return UserSerializer(instance=obj.upload_author, many=False).data

    def get_category(self, obj):
        # book = obj
        # print(f"book: {book} | {type(book)}")
        # categories = obj.category
        # print(f"categories: {categories} | {type(categories)}")
        # for category in categories.all():
        #     print(f"category: {category} | {type(category)}")

        # print(obj.created_datetime_field)
        # print(obj.update_datetime_field)

        list1 = []
        for obj in obj.category.all():
            serialized_obj_list = BookCategorySerializer(instance=obj, many=False).data
            list1.append(serialized_obj_list)
        return list1

    def get_category2(self, obj):
        return BookCategorySerializer(instance=obj.category.all(), many=True).data

    def get_profile2(self, obj):

        # author_username = obj.upload_author.username  # admin
        # user = User.objects.get(username=author_username)
        # profile = models.Profile.objects.get(user=obj.upload_author)

        return ProfileSerializer(instance=models.Profile.objects.get(user=obj.upload_author), many=False).data


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelBookCategory
        fields = '__all__'

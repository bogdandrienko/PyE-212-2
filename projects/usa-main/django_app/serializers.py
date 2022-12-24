from rest_framework import serializers
from django_app import models
from django.contrib.auth.models import User
#

class ProfileModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    user_id = serializers.ReadOnlyField(source = 'user.id')
    avatar = serializers.ImageField(required=False)
    class Meta:
        model = models.Profile
        # fields = ['id', 'user', 'user_id', 'avatar']
        fields = "__all__"



class UserModelSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        # fields = ['pk', 'username', 'email']
        
    def get_avatar(self, obj):
        obj_list =  models.Profile.objects.filter(pk = obj.pk)

        return ProfileModelSerializer(instance=obj_list, many=True).data

class VideoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.youtube_video
        fields = "__all__"


class VideoCategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.youtube_video_category
        fields = "__all__"
        


# картинка тест
class MyPostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model =models.MyPost
        fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']
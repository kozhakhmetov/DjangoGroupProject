from users.serializers import UserSerializer
from core.models import Post
from rest_framework import serializers


class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'created_at', 'header', 'created_by', 'description')
        read_only_fields = ('id', 'created_at', 'created_by')


class OwnPostSerializer(BasePostSerializer):

    class Meta:
        model = Post
        fields = BasePostSerializer.Meta.fields + ('views', 'liked_by')
        read_only_fields = BasePostSerializer.Meta.read_only_fields + ('views', 'liked_by')



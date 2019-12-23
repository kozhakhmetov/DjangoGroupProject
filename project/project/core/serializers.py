from users.serializers import UserSerializer
from core.models import Post, Comment
from utils.constants import CATEGORIES
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

    def validate_category(self, category):
        if category not in CATEGORIES.keys():
            raise serializers.ValidationError('Category is not correct')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'created_by')
from users.serializers import UserSerializer
from core.models import Post, PostSaved, Comment, Subscription
from utils.constants import CATEGORIES
from rest_framework import serializers


class BasePostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField('get_like_count')

    class Meta:
        model = Post
        fields = ('id', 'category', 'created_at', 'header', 'created_by', 'description', 'like_count')
        read_only_fields = ('id', 'created_at', 'created_by', 'like_count')

    def get_like_count(self, post):
        return post.liked_by.count()


class OwnPostSerializer(BasePostSerializer):

    class Meta:
        model = Post
        fields = BasePostSerializer.Meta.fields + ('views', 'liked_by')
        read_only_fields = BasePostSerializer.Meta.read_only_fields + ('views', 'liked_by')

    def validate_category(self, category):
        if category not in CATEGORIES.keys():
            raise serializers.ValidationError('Category is not correct')

class BasePostSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',)


class SavedPostSerializer(serializers.Serializer):
    post = BasePostSerializer()


class SavedPostSerializerSave(serializers.Serializer):
    def create(self, validated_data):
        post_saved = PostSaved(**validated_data)
        post_saved.save()
        return post_saved

    #post = BasePostSerializerSave()
    # saved_by =


class BaseCommentSerializer(serializers.ModelSerializer):
    post = BasePostSerializerSave

    class Meta:
        model = Comment
        fields = ('id', 'post', 'reply_to', 'created_by', 'created_at', 'content')
        read_only_fields = ('id', 'created_by', 'created_at')


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fieds = ('id', 'userFrom')
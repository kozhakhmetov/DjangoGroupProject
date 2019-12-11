from users.serializers import UserSerializer
from core.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'description', 'created_by', 'views', 'category', 'created_at')
        read_only_fields = ('created_at', 'author',)

        def create(self, validated_data):
            post = Post(**validated_data)
            post.save()
            return post


class PostSerializerFull:
    pass

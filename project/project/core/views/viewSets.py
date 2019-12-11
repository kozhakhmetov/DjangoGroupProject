from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Post, Comment
from core.serializers import PostSerializer, PostSerializerFull
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action


class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)
    search_fields = ('description',)
    ordering_fields = ('created_at',)
    ordering = ('-created_at',)

    def get_queryset(self):
        if self.action == 'list':
            return Post.user_posts.subscribers_posts(self.request.user)
        return Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        elif self.action == 'retrieve':
            return PostSerializerFull
        return PostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    @action(methods=['GET'], detail=False)
    def my_posts(self, request):
        posts = Post.user_posts.created_by_user(self.request.user)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def my_saved(self, request):
        posts = Post.user_posts.user_saved(self.request.user)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

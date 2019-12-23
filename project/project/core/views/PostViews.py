from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import Post
from core.serializers import BasePostSerializer, OwnPostSerializer
from rest_framework.decorators import action


class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.posts.all()
    serializer_class = BasePostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class OwnPostViewSet(viewsets.ModelViewSet):
    queryset = Post.posts.all()
    serializer_class = OwnPostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        posts = Post.posts.created_by_user(request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)








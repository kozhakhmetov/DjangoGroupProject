from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import Post, Subscription, PostSaved
from core.serializers import BasePostSerializer, OwnPostSerializer, SavedPostSerializer, SavedPostSerializerSave
from rest_framework.views import APIView

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

class SavedPostCreateListDelete(APIView):

    http_method_names = ['get', 'post']

    def get(self, request):
        saved_posts = PostSaved.post_saved.get_user_saved(request.user)
        serializer = SavedPostSerializer(saved_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavedPostSerializerSave(data=request.data)
        if serializer.is_valid():
            post = Post.posts.get(pk=request.data['post_id'])
            serializer.save(saved_by=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


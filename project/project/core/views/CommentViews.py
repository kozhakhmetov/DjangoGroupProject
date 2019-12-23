from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from core.models import Post, PostSaved, Comment
from core.serializers import BaseCommentSerializer
from rest_framework.decorators import action


class CommentListViewSet(mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):

    queryset = Comment.comments.all()
    serializer_class = BaseCommentSerializer

    @action(methods=['get'], detail=True)
    def comment_to_post(self, request, pk):
        comments = Comment.comments.filter(post=pk)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = BaseCommentSerializer

    def get_queryset(self):
        return Comment.comments.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import Post, Subscription
from core.serializers import BasePostSerializer, OwnPostSerializer, SubscriptionSerializer
from rest_framework.decorators import action
from users.models import MainUser

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


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.subscriptions.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(userFrom=self.request.user)

    @action(methods=['GET'], detail=True)
    def subscription_of_user(self, request, pk):
        user = MainUser.objects.get(pk=id)
        subscriptions = Subscription.subscriptions.get_user_subscriptions(user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)


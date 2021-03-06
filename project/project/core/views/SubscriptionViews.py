from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from core.models import Subscription
from core.serializers import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)

class SubscriptionListViewSet(mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = Subscription.subscriptions.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True)
    def subscription_of_user(self, request, pk):
        subscriptions = Subscription.subscriptions.get_user_subscriptions(user=pk)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        logger.info(f"{self.request.user} to {self.request.data['userTo']}")
        subscriptions = Subscription.objects.all().filter(userFrom=self.request.user)
        for i in subscriptions:
            if self.request.data['userTo'] == i.userTo.id:
                logger.error(f"{self.request.user} has such subscription !!!")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        logger.info(f"{self.request.user} created new subscription")
        return serializer.save(userFrom=self.request.user)

    def get_queryset(self):
        return Subscription.objects.all().filter(userFrom=self.request.user)
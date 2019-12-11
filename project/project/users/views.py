from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer, ProfileSerializer
from users.models import MainUser, Profile


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class RegisterUserAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MainUser.objects.filter(is_deleted=0)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


# class ProfileViewSet(mixins.RetrieveModelMixin,
#                      mixins.ListModelMixin,
#                      mixins.DestroyModelMixin,
#                      mixins.UpdateModelMixin,
#                      viewsets.GenericViewSet):
#     queryset = Profile.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProfileSerializer
#
#     def get_serializer_class(self):
#         if self.action == 'get_queryset':
#             return ProfileGetSerializer
#         return ProfileSerializer
#
#     def get_queryset(self):
#         return self.queryset.all()
#
#     def update(self, request, *args, **kwargs):
#         profile = Profile.objects.get(user=request.user)
#         profile.bio = request.data['bio']
#         profile.avatar = request.data['avatar']
#         profile.save()
#         serializer = ProfileGetSerializer(profile)
#         return Response(serializer.data)

from rest_framework import serializers
from users.models import MainUser, Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        # Profile.objects.create(data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio')
#
#
# class ProfileGetSerializer(serializers.Serializer):
#     bio = serializers.CharField(max_length=255)
#     avatar = serializers.FileField(allow_null=True)
#     user = UserSerializer()
#
#     def create(self, validated_data):
#         profile = Profile.objects.create(**validated_data)
#         return profile
#
#     def update(self, instance, validated_data):
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#
#         instance.save()
#         return instance

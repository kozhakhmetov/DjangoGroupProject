from rest_framework import serializers
from users.models import MainUser, Profile
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        read_only_fields = ('id',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        with transaction.atomic():
            user = MainUser.objects.create_user(**validated_data)
            user.save()
            return user

    def validate_password(self, password):
        if len(password) < 4:
            raise serializers.ValidationError('length should be at least 4')
        if password.contains(' '):
            raise serializers.ValidationError('password should not have any spaces')
        if not any(c.isdigit() for c in password):
            raise serializers.ValidationError('password should have at least one digit')



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = '__all__'
        read_only_fields = ('user', )

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance

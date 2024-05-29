from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserSettings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('role',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        UserSettings.objects.create(user=user)

        return user


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['id', 'expected_pages_per_day']

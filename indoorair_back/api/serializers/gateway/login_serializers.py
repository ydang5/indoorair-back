from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        request=self.context.get(request)
        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return user
        except Exception as e:
            print(e)
        raise serializers.ValidationError('Please enter valid username and password')

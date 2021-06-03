from . import models
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class SendConfirmationCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        fields = [
            'email',
        ]
        model = User


class SendTokenSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=40)

    class Meta:
        fields = [
            'email',
            'confirmation_code',
        ]
        model = User

    @staticmethod
    def get_token(user):
        return RefreshToken.for_user(user)

    def validate(self, data):
        email = data['email']
        confirmation_code = data.get('confirmation_code')
        user = get_object_or_404(
            User,
            email=email,
        )
        if user.confirmation_code != confirmation_code:
            raise exceptions.ValidationError('invalid confirmation code')
        else:
            token = self.get_token(user)
            data['token'] = str(token.access_token)
        return data


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    role = serializers.ReadOnlyField(required=False)

    class Meta:
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        ]
        model = User

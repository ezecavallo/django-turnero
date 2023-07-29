"""tokens serializers"""
# pylint: disable=W0223

# Django
from django.contrib.auth import get_user_model

# REST Framework
from rest_framework import serializers

# Knox
from knox.models import AuthToken

from dj_rest_auth.serializers import UserDetailsSerializer


class UserDetailsCustomSerializer(UserDetailsSerializer):
    """
    Custom User Detail serializer.
    """

    class Meta:
        """Meta class"""
        UserModel = get_user_model()
        model = UserModel
        fields = [
            UserModel.EMAIL_FIELD,
            "first_name",
            "last_name"
        ]


class KnoxSerializer(serializers.Serializer):
    """
    Serializer for Knox authentication.
    """
    token = serializers.SerializerMethodField()
    user = UserDetailsCustomSerializer()

    def get_token(self, obj):
        """Get token"""
        return obj["token"][1]


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        """Meta class"""
        model = AuthToken
        fields = ('token_key',)

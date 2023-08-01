"""Business serializers"""

# REST Framework
from rest_framework import serializers

# Serializers
from core.subscriptions.serializers import CustomerSerializer


class BusinessPublicSerializer(serializers.Serializer):
    """Business serializer"""

    name = serializers.CharField(read_only=True)
    slug_name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    open_hours = serializers.JSONField(read_only=True)
    logo = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BusinessSerializer(serializers.Serializer):
    """Business serializer"""

    name = serializers.CharField(read_only=True)
    slug_name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    open_hours = serializers.JSONField(read_only=True)
    logo = serializers.CharField(read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, instance):
        """Get subscription"""
        subscription = instance.subscription
        return CustomerSerializer(subscription, read_only=True).data

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BusinessUpdateSerializer(serializers.Serializer):
    """Business serializer"""

    name = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    open_hours = serializers.JSONField()
    logo = serializers.CharField()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

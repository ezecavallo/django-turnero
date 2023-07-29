"""Subscriptions serializers"""

# REST Framework
from rest_framework import serializers


class SubscriptionSerializer(serializers.Serializer):
    """Subscription serializer"""

    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

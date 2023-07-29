"""Customers serializers"""

# REST Framework
from rest_framework import serializers

# Models
from core.subscriptions.models import Customer


class CustomerSerializer(serializers.Serializer):
    """Customer serializer"""

    uuid = serializers.CharField(read_only=True)
    date_billing_start = serializers.DateTimeField(read_only=True)
    date_billing_end = serializers.DateTimeField(read_only=True)
    state = serializers.ChoiceField(read_only=True, choices=Customer.STATE)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

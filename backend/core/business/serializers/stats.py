"""Business stats serializers"""

# REST Framework
from rest_framework import serializers


class BusinessStatsSerializer(serializers.Serializer):
    """Business serializer"""

    total_events = serializers.SerializerMethodField()
    events_per_book = serializers.SerializerMethodField()
    total_clients = serializers.SerializerMethodField()

    def get_total_events(self, instance):
        """Get total events"""
        return self.instance.get_total_events()

    def get_events_per_book(self, instance):
        """Get events per book"""
        return (self.instance.get_total_events() / self.instance.get_total_books())

    def get_total_clients(self, instance):
        """Get total events"""
        return self.instance.get_total_clients()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

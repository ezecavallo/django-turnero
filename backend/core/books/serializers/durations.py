"""Durations serializers"""

# REST Framework
from rest_framework import serializers

# Models


class BookCreate(serializers.Serializer):
    """Book creation serializer"""

    duration = serializers.IntegerField()
    book = serializers.HiddenField(default='')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

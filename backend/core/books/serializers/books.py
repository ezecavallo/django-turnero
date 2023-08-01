"""Books serializers"""

# REST Framework
from rest_framework import serializers

# Models
from core.books.models import Book, Duration
import uuid as uuuid


class DurationSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    duration = serializers.IntegerField()
    price = serializers.IntegerField()


class BookAdminSerializer(serializers.Serializer):
    """Book Admin serializer"""

    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    deposit_percentage = serializers.IntegerField(read_only=True)
    durations = DurationSerializer(
        many=True,
        read_only=True,
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BookPublicSerializer(serializers.Serializer):
    """Book Public serializer"""

    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    deposit_percentage = serializers.IntegerField(read_only=True)
    durations = DurationSerializer(
        many=True,
        read_only=True,
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BookCreate(serializers.Serializer):
    """Book creation serializer"""

    name = serializers.CharField(max_length=150)
    deposit_percentage = serializers.IntegerField(max_value=100, min_value=0)
    business = serializers.HiddenField(default='')

    def create(self, validated_data):
        """Create book object"""

        validated_data.pop("business")
        business = self.context.get("business")

        instance = Book.objects.create(**validated_data, business=business)
        return instance

    def update(self, instance, validated_data):
        pass


class BookUpdate(serializers.Serializer):
    """Book update serializer"""

    name = serializers.CharField(max_length=150)
    deposit_percentage = serializers.IntegerField(max_value=100, min_value=0)
    durations = DurationSerializer(
        many=True
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        """Update book object"""
        durations = validated_data.pop("durations", False)
        if durations:
            for duration in durations:
                values = dict(duration)
                uuid = values.get("uuid")
                time = values.get("duration")
                Duration.objects.update_or_create(uuid=uuid, book=instance, defaults={
                    "duration": time, "uuid": str(uuuid.uuid4())
                })

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

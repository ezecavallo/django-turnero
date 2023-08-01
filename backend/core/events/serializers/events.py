"""Events serializers"""

# Django
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# REST Framework
from rest_framework import serializers

# Models
from core.books.models import Duration
from core.events.models import Event

# Exceptions
from core.events import exceptions


class EventValidation(serializers.Serializer):
    """Event validate serializer"""

    start_at = serializers.DateTimeField()
    close_at = serializers.DateTimeField()
    duration = serializers.HiddenField(default='')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        business = self.context.get('business')
        self.fields['duration'] = serializers.SlugRelatedField(
            slug_field='uuid',
            queryset=Duration.objects.filter_by_business(business)
        )

    def validate(self, attrs):
        """Validate event"""

        start_at = attrs.get('start_at')
        close_at = attrs.get('close_at')
        duration = attrs.get('duration')
        self.book = duration.book
        print(start_at, close_at)
        print(duration)
        print(self.book)
        # Validate valid hours
        events = Event.objects.filter_by_book(self.book).filter_in_between_hours(start_at, close_at)
        if events:
            raise exceptions.ConflictSchedule(_("The event has schedule conflicts."))

        # Validate valid context hours in schedule
        previous_event = Event.objects.filter_by_book(self.book).filter_previous_event(start_at).first()
        if previous_event:
            min_duration = Duration.objects.filter_by_book(self.book).get_min_duration()
            time_between_events = abs((previous_event.close_at - start_at).total_seconds() / 60)
            if time_between_events < min_duration:
                raise exceptions.ConflictSchedule(_("The start time is invalid."))

        # Validate valid duration
        duration_amount = abs(start_at - close_at).total_seconds() / 60
        is_valid_duration = Duration.objects.filter_by_book(self.book).filter(duration=duration_amount)
        if not is_valid_duration:
            raise exceptions.InvalidDuration(_("The event has an invalid duration."))

        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EventAdminSerializer(serializers.Serializer):
    """Event Admin serializer"""

    uuid = serializers.UUIDField(read_only=True)
    book = serializers.SlugRelatedField(
        slug_field='uuid',
        read_only=True
    )
    start_at = serializers.DateTimeField(read_only=True)
    close_at = serializers.DateTimeField(read_only=True)

    price = serializers.DecimalField(
        max_digits=24,
        min_value=0,
        decimal_places=2,
        read_only=True
    )
    paid = serializers.BooleanField(read_only=True)
    deposit_amount = serializers.DecimalField(
        max_digits=24,
        min_value=0,
        decimal_places=2,
        read_only=True
    )
    deposit_paid = serializers.BooleanField(read_only=True)

    email = serializers.EmailField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    issued_by = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EventPublicSerializer(serializers.Serializer):
    """Event Public serializer"""

    uuid = serializers.UUIDField(read_only=True)
    book = serializers.SlugRelatedField(
        slug_field='uuid',
        read_only=True
    )
    start_at = serializers.DateTimeField(read_only=True)
    close_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EventCreate(EventValidation):
    """Event creation serializer"""

    start_at = serializers.DateTimeField()
    close_at = serializers.DateTimeField()
    price = serializers.HiddenField(default='')

    email = serializers.EmailField()
    phone_number = serializers.CharField()
    issued_by = serializers.HiddenField(default='')

    def create(self, validated_data):
        """Create event"""

        validated_data.pop("price")
        duration = validated_data.pop("duration")
        print(duration)
        price = duration.price
        deposit_amount = price * self.book.deposit_percentage / 100 or 0

        validated_data.pop("issued_by")
        user = self.context.get("request").user

        instance = Event.objects.create(
            **validated_data,
            price=price,
            book=self.book,
            deposit_percentage=self.book.deposit_percentage,
            deposit_amount=deposit_amount,
            issued_by=user if user.is_authenticated else None
        )
        return instance

    def update(self, instance, validated_data):
        pass


class EventCreateByAdmin(EventValidation):
    """Event creation by admin serializer"""

    start_at = serializers.DateTimeField()
    close_at = serializers.DateTimeField()

    email = serializers.EmailField()
    phone_number = serializers.CharField()
    issued_by = serializers.SlugRelatedField(
        slug_field="email",
        queryset=get_user_model().objects.all()
    )

    def create(self, validated_data):
        """Create event by admin"""

        validated_data.pop("price")
        book = validated_data.get("book")
        price = book.price
        deposit_amount = price * book.deposit_percentage / 100 or 0

        validated_data.pop("issued_by")
        user = self.context.get("request").user

        instance = Event.objects.create(
            **validated_data,
            price=price,
            deposit_percentage=book.deposit_percentage,
            deposit_amount=deposit_amount,
            issued_by=user if user else None
        )
        return instance

    def update(self, instance, validated_data):
        pass


class EventUpdate(EventValidation):
    """Event update serializer"""

    email = serializers.EmailField()
    phone_number = serializers.CharField()
    issued_by = serializers.SlugRelatedField(
        slug_field="email",
        queryset=get_user_model().objects.all()
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

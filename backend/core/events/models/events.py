"""Business models"""

# Utils
from datetime import datetime

# Django
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import RangeOperators, DateTimeRangeField

# Models
from core.utils.models import BaseModel
from core.books.models import Book
from core.business.models import Business


class EventQuerySet(models.query.QuerySet):
    """Event QuerySet"""

    def filter_by_business(self, business: Business):
        """Filter by business"""
        return self.filter(book__business=business)

    def filter_by_book(self, book: Book):
        """Filter by book"""
        return self.filter(book=book)

    def filter_previous_event(self, start_at: datetime):
        """Filter previous event"""
        return self.filter(
            close_at__date=start_at.date(),
            close_at__lte=start_at
        ).order_by('-close_at')

    def filter_in_between_hours(self, start_at: datetime, close_at: datetime):
        """Filter in between hours"""
        return self.filter(
            # Check if exists an Event STARTS between the given hours
            models.Q(start_at__gt=start_at, start_at__lt=close_at) |
            # Check if exists an Event ENDS between the given hours
            models.Q(close_at__gt=start_at, close_at__lt=close_at) |
            # Check if exists an Event is INSIDE the given hours
            models.Q(start_at__lt=start_at, close_at__gt=close_at) |
            # Check if exists an Event is INSIDE and END equal to the given hours
            models.Q(start_at__lt=start_at, close_at__gte=close_at) |
            # Check if exists an Event is INSIDE the given hours
            models.Q(start_at__lte=start_at, close_at__gte=close_at)
        )


class Event(BaseModel):
    """
    Event model
    """

    email = models.EmailField(blank=False)
    phone_number = models.CharField(
        "phone number",
        blank=True,
        max_length=16,
        validators=[
            RegexValidator(
                regex=r'\+?1?\d{9,15}$',
                # pylint: disable=line-too-long
                message=_("Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.")
            )
        ]
    )
    issued_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="events",
        null=True,
        blank=True
    )

    start_at = models.DateTimeField()
    close_at = models.DateTimeField()

    price = models.DecimalField(
        _("price"),
        max_digits=24,
        decimal_places=14,
        default=0,
        help_text=_("The price of the event."),
        validators=[
            MinValueValidator(0)
        ]
    )
    paid = models.BooleanField(
        _("paid"),
        default=False,
    )

    deposit_percentage = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    deposit_amount = models.DecimalField(
        _("deposit amount"),
        max_digits=24,
        decimal_places=14,
        default=0,
        help_text=_("The amount for this deposit transaction only."),
        validators=[
            MinValueValidator(0)
        ]
    )
    deposit_paid = models.BooleanField(
        _("deposit paid"),
        default=False,
    )

    book = models.ForeignKey(
        "books.Book",
        related_name="events",
        on_delete=models.PROTECT,
    )

    objects = EventQuerySet.as_manager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False, phone_number__isnull=False)
                | models.Q(issued_by__isnull=False),
                name='not_both_null'
            ),
            ExclusionConstraint(
                name="exclude_overlapping_datetimes",
                expressions=[
                    (models.Func("start_at", "close_at", function="tstzrange",
                                 output_field=DateTimeRangeField()), RangeOperators.OVERLAPS),
                    ('book', RangeOperators.EQUAL),
                ],
            )
        ]

    def __str__(self):
        """Return event"""
        return f"{self.start_at}, {self.close_at}"


class EventManager(models.Manager):
    pass

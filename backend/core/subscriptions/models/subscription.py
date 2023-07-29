"""Subscriptions models"""

# Utils
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Models
from core.utils.models import BaseModel


class Subscription(BaseModel):
    """
    Subscription model
    """

    ONCE = '0'
    SECOND = '1'
    MINUTE = '2'
    HOUR = '3'
    DAY = '4'
    WEEK = '5'
    MONTH = '6'
    YEAR = '7'
    RECURRENCE_UNIT_CHOICES = (
        (ONCE, 'once'),
        (SECOND, 'second'),
        (MINUTE, 'minute'),
        (HOUR, 'hour'),
        (DAY, 'day'),
        (WEEK, 'week'),
        (MONTH, 'month'),
        (YEAR, 'year'),
    )

    recurrence_period = models.PositiveSmallIntegerField(
        default=1,
        help_text=_('how often the plan is billed (per recurrence unit)'),
        validators=[MinValueValidator(1)],
    )
    recurrence_unit = models.CharField(
        choices=RECURRENCE_UNIT_CHOICES,
        default=MONTH,
        max_length=1,
    )

    plan = models.ForeignKey(
        "subscriptions.Plan",
        help_text=_('the subscription plan for these cost details'),
        on_delete=models.CASCADE,
        related_name='costs',
    )
    price = models.DecimalField(
        _("price"),
        max_digits=24,
        decimal_places=14,
        help_text=_("The default price for events of this book."),
        validators=[
            MinValueValidator(0)
        ]
    )

    class Meta:
        ordering = ('recurrence_unit', 'recurrence_period', 'price',)

    def __str__(self):
        """Return subscription"""
        return f"{self.recurrence_period}: {self.price}"

    def next_billing_datetime(self, current):
        """Calculates next billing date for provided datetime.
            Parameters:
                current (datetime): The current datetime to compare
                    against.
            Returns:
                datetime: The next time billing will be due.
        """
        if self.recurrence_unit == self.SECOND:
            delta = relativedelta(seconds=self.recurrence_period)
        elif self.recurrence_unit == self.MINUTE:
            delta = relativedelta(minutes=self.recurrence_period)
        elif self.recurrence_unit == self.HOUR:
            delta = relativedelta(hours=self.recurrence_period)
        elif self.recurrence_unit == self.DAY:
            delta = relativedelta(days=self.recurrence_period)
        elif self.recurrence_unit == self.WEEK:
            delta = relativedelta(weeks=self.recurrence_period)
        elif self.recurrence_unit == self.MONTH:
            delta = relativedelta(months=self.recurrence_period)
        elif self.recurrence_unit == self.YEAR:
            delta = timedelta(years=self.recurrence_period)
        else:
            # If no recurrence period, no next billing datetime
            return None

        return current + delta

"""Event Logging models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.utils.models import BaseModel


class EventLogging(BaseModel):
    """
    EventLogging model
    """

    VERBS = (
        ('CR', 'Created'),
        ('UP', 'Updated'),
        ('DE', 'Deleted'),
        ('CA', 'Cancelled'),
        ('CO', 'Completed'),
        ('PA', 'Paid'),
        ('PP', 'Parcially Paid'),
    )

    verb = models.CharField(
        _("action"),
        max_length=10,
    )

    event = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name="loggings"
    )

    def __str__(self):
        """Return event logging"""
        return f"asd"

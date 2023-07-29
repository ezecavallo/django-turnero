"""Utils models"""

# Utils
import uuid

# Django
from django.db import models


class BaseModel(models.Model):
    """
    Base abstract model

    This class provides:
        + created (Datetime)
        + modified (Datetime)
    """

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    created = models.DateTimeField(
        'creted_at',
        auto_now_add=True,
        help_text='Datetime on which the object was created'
    )
    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='Datetime on which the object was modified'
    )

    class Meta:
        """Meta class"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']

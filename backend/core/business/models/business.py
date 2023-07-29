"""Business models"""

# Utils
from typing import List

# Django
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.apps import apps

# Models
# from core.events.models import Event
from core.users.models import User
from core.utils.models import BaseModel

# Validators
from core.utils.validators import JSONFieldSchemaValidator


class BusinessQuerySet(models.query.QuerySet):
    """Business QuerySet"""

    def filter_by_members(self, users: List[User]):
        """Filter business by their members"""
        return self.filter(members__in=users)


class Business(BaseModel):
    """
    Business model
    """

    schema = {
        "type": "object",
        "properties": {
            "monday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "tuesday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "wednesday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "thursday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "friday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "saturday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
            "sunday": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "time"
                }
            },
        },
        "required": [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ],
    }

    name = models.CharField(_("business name"), max_length=150, blank=False)

    slug_name = models.SlugField(unique=True, max_length=50, blank=False)

    address = models.CharField(_("business address"), max_length=150, blank=False)

    email = models.EmailField(blank=False)

    phone_number = models.CharField(
        _("phone number"),
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

    logo = models.ImageField(
        upload_to='business/logo',
    )

    open_hours = models.JSONField(
        _("open hours"),
        validators=[JSONFieldSchemaValidator(schema)],
        default={
            "monday": ["08:00:00", "21:00:00"],
            "tuesday": ["08:00:00", "21:00:00"],
            "wednesday": ["08:00:00", "21:00:00"],
            "thursday": ["08:00:00", "21:00:00"],
            "friday": ["08:00:00", "21:00:00"],
            "saturday": ["08:00:00", "21:00:00"],
            "sunday": ["08:00:00", "21:00:00"]
        }

    )

    subscription = models.OneToOneField(
        "subscriptions.Customer",
        on_delete=models.SET_NULL,
        related_name="business",
        null=True,
        blank=True
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_staff': True},
        related_name="business",
        blank=True
    )

    objects = BusinessQuerySet.as_manager()

    def get_total_events(self):
        """Get total events of business"""
        return apps.get_model("events", "Event").objects.filter_by_business(self).count()

    def get_total_clients(self):
        """Get total unique clients of business"""
        return apps.get_model("events", "Event")\
            .objects.filter_by_business(self).values("email").distinct().count()

    def get_total_books(self):
        """Get total unique clients of business"""
        return self.books.all().count()

    def __str__(self):
        """Return business name"""
        return str(self.name)

"""Subscriptions apps."""

# Django
from django.apps import AppConfig


class SubscriptionsAppConfig(AppConfig):
    """Subscriptions app config"""

    name = 'core.subscriptions'
    verbose_name = 'Subscriptions'
    default_auto_field = 'django.db.models.AutoField'

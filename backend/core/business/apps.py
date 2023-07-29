"""Business apps."""

# Django
from django.apps import AppConfig


class BusinessAppConfig(AppConfig):
    """Business app config"""

    name = 'core.business'
    verbose_name = 'Business'
    default_auto_field = 'django.db.models.AutoField'

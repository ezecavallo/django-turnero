"""Events apps."""

# Django
from django.apps import AppConfig


class EventsAppConfig(AppConfig):
    """Events app config"""

    name = 'core.events'
    verbose_name = 'Events'
    default_auto_field = 'django.db.models.AutoField'

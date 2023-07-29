"""Users apps."""

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Users app config"""

    name = 'core.users'
    verbose_name = 'Users'
    default_auto_field = 'django.db.models.AutoField'

"""Books apps."""

# Django
from django.apps import AppConfig


class BooksAppConfig(AppConfig):
    """Books app config"""

    name = 'core.books'
    verbose_name = 'Books'
    default_auto_field = 'django.db.models.AutoField'

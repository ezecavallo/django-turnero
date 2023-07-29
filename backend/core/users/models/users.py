"""users models"""

# Utils
import uuid

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model.
    Based on Django abstract model.
    """

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    first_name = None
    last_name = None
    full_name = models.CharField(max_length=150, blank=False)

    email = models.EmailField(
        'email',
        unique=True,
        help_text={
            'unique': 'A user with that email alreay exists.'
        }
    )

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user has verfied his email adress.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    def __str__(self):
        """Return username."""
        return self.email

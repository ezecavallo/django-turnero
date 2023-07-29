# pylint: disable = missing-class-docstring
"""Event exceptions"""

from django.core.exceptions import ValidationError


class ConflictSchedule(ValidationError):
    pass


class InvalidDuration(ValidationError):
    pass

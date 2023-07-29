"""Durations models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.utils.models import BaseModel
from core.books.models import Book


class DurationQuerySet(models.query.QuerySet):
    """Duration QuerySet"""

    def filter_by_book(self, book: Book):
        """Filter by book"""
        return self.filter(book=book)

    def get_min_duration(self):
        """Get min duration value"""
        return self.aggregate(models.Min('duration')).get('duration__min', 0)


class Duration(BaseModel):
    """
    Duration model
    """

    duration = models.PositiveSmallIntegerField(_("durations"))

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="durations"
    )

    objects = DurationQuerySet.as_manager()

    class Meta:
        unique_together = [["duration", "book"]]

    def __str__(self):
        """Return book"""
        return str(self.duration)

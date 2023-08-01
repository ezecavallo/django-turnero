"""Durations models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Models
from core.utils.models import BaseModel
from core.books.models import Book
from core.business.models import Business


class DurationQuerySet(models.query.QuerySet):
    """Duration QuerySet"""

    def filter_by_business(self, business: Business):
        """Filter by business"""
        return self.filter(book__business=business)

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

    price = models.DecimalField(
        _("price"),
        max_digits=24,
        decimal_places=14,
        help_text=_("The default price for events of this duration."),
        validators=[
            MinValueValidator(0)
        ]
    )

    objects = DurationQuerySet.as_manager()

    class Meta:
        unique_together = [["duration", "book"]]

    def __str__(self):
        """Return book"""
        return str(self.duration)

"""Books models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Models
from core.utils.models import BaseModel
from core.business.models import Business


class BookQuerySet(models.query.QuerySet):
    """Book QuerySet"""

    def filter_by_business(self, business: Business):
        """Filter by business"""
        return self.filter(business=business)


class Book(BaseModel):
    """
    Book model
    """

    name = models.CharField(_("book name"), max_length=150)

    is_active = models.BooleanField(default=True)

    deposit_percentage = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    business = models.ForeignKey(
        "business.Business",
        on_delete=models.PROTECT,
        related_name="books"
    )

    objects = BookQuerySet.as_manager()

    def __str__(self):
        """Return book"""
        return str(self.name)

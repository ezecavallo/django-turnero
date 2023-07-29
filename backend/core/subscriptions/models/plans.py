"""Plans models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.utils.models import BaseModel


class Plan(BaseModel):
    """
    Plan model
    """

    plan_name = models.CharField(
        _("name"),
        max_length=64,
        blank=False,
        help_text=_('the name of the subscription plan'),
    )
    slug = models.SlugField(
        help_text=_('slug to reference the subscription plan'),
        max_length=128,
        null=True,
        blank=True,
        unique=True,
    )
    description = models.CharField(_("description"), max_length=128, blank=True)

    class Meta:
        ordering = ('plan_name',)

    def __str__(self):
        """Return plan"""
        return f"{self.plan_name}"

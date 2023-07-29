"""Customers models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.utils.models import BaseModel


class Customer(BaseModel):
    """
    Customer model
    """

    ERROR = 0
    ACTIVE = 1
    EXPIRED = 2
    ENDED = 3

    STATE = (
        (ERROR, "error"),
        (ACTIVE, "active"),
        (EXPIRED, "expired"),
        (ENDED, "ended"),
    )

    date_billing_start = models.DateTimeField(
        blank=True,
        help_text=_('the date to start billing this subscription'),
        null=True,
        verbose_name='billing start date',
    )
    date_billing_end = models.DateTimeField(
        blank=True,
        help_text=_('the date to finish billing this subscription'),
        null=True,
        verbose_name='billing start end',
    )
    date_billing_last = models.DateTimeField(
        blank=True,
        help_text=_('the last date this plan was billed'),
        null=True,
        verbose_name='last billing date',
    )
    date_billing_next = models.DateTimeField(
        blank=True,
        help_text=_('the next date billing is due'),
        null=True,
        verbose_name='next start date',
    )

    subscription = models.ForeignKey(
        "subscriptions.Subscription",
        on_delete=models.PROTECT,
        related_name="customers"
    )

    state = models.IntegerField(
        _("state"),
        choices=STATE,
        default=ACTIVE
    )

    def __str__(self):
        """Return customer"""
        return f"{self.subscription}, {self.state}"

    def cancel_autorenew(self):
        """Cancel auto renew"""
        pass

    def renew(self):
        """Renew"""
        pass

    def end_subscruption(self):
        """"End subscription"""
        pass

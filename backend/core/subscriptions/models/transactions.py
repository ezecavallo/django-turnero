"""Suscriptions transactions models"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Models
from core.utils.models import BaseModel


class SubscriptionTransaction(BaseModel):
    """
    Transactions model
    """

    TRANSACTION_TYPE = (
        ("DE", _("Deposit")),
        ("PA", _("Total pay")),
    )

    type = models.CharField(
        _("type"),
        choices=TRANSACTION_TYPE,
        max_length=2
    )

    transaction_amount = models.DecimalField(
        _("transaction amount"),
        max_digits=24,
        decimal_places=14,
        default=0,
        help_text=_("The amount for this transaction only."),
        validators=[
            MinValueValidator(0)
        ]
    )

    customer = models.ForeignKey(
        "subscriptions.Customer",
        on_delete=models.PROTECT,
        related_name="transactions"
    )

    payment = models.OneToOneField(
        "mercadopago.PaymentMercadoPago",
        on_delete=models.PROTECT,
        related_name="subscription_transaction"
    )

    def __str__(self):
        """Return book"""
        return f"<Transaction: ${self.transaction_amount}, {self.type}, {self.event}"

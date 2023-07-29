"""Subscriptions models admin."""

# Django
from django.contrib import admin

# Models
from core.subscriptions import models


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ('recurrence_period', 'recurrence_unit')


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    """Plan model admin."""

    list_display = ('plan_name', 'slug')


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer model admin."""

    list_display = ('date_billing_start', 'date_billing_end', 'state')

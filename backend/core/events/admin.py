"""Events models admin."""

# Django
from django.contrib import admin

# Models
from core.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ('email', 'issued_by', 'start_at', 'close_at', 'price', 'paid')

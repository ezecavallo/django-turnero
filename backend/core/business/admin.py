"""Companies models admin."""

# Django
from django.contrib import admin

# Models
from core.business.models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    """Business model admin."""

    list_display = ('name', 'slug_name', 'address', 'email')
    filter_horizontal = ('members',)

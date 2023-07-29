"""Book models admin."""

# Django
from django.contrib import admin

# Models
from core.books.models import Book, Duration


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book model admin."""

    list_display = ('name', 'is_active')


@admin.register(Duration)
class DurationAdmin(admin.ModelAdmin):
    """Duration model admin."""

    list_display = ('duration',)

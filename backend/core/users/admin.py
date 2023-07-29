"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

# Models
from core.users.models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'full_name', )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """User model admin."""

    add_form = UserCreateForm
    list_display = ('email', 'username', 'full_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'is_active')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("full_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'username', 'password1', 'password2', ),
        }),
    )

"""Utils permissions"""

# Utils
from copy import deepcopy

# REST Framework
from rest_framework.permissions import BasePermission, DjangoModelPermissions


class IsSuperUser(BasePermission):
    """Superuser permission."""

    def has_permission(self, request, view):
        """Check if user is superuser."""
        return bool(request.user and request.user.is_superuser)


class CustomDjangoModelPermissions(DjangoModelPermissions):
    """Superuser permission."""

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

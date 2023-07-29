"""Companies permissions"""

# REST Framework
from rest_framework.permissions import BasePermission


class IsAdminOrBusinessMemberObject(BasePermission):
    """
    Check permission for staff or business members.
    """

    def has_object_permission(self, request, view, obj):
        """Check if user is business member or superuser"""

        return bool(request.user and request.user.is_superuser) or request.user in obj.members.all()


class IsAdminOrBusinessMember(BasePermission):
    """
    Check permission for staff or business members.
    """

    def has_permission(self, request, view):
        """Check if user is business member or superuser"""

        return bool(request.user and request.user.is_superuser) or request.user in view.business.members.all()

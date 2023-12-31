"""Business views"""

# REST Framework
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny
from core.business.permissions import IsAdminOrBusinessMemberObject
from core.utils.permissions import CustomDjangoModelPermissions

# Models
from core.business.models import Business

# Serializers
from core.business import serializers


class BusinessModelViewSet(viewsets.GenericViewSet,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin):
    """
    ViewSet Model for viewing and editing business.
    """
    serializer_class = serializers.BusinessSerializer
    # permission_classes = []
    permission_classes = []
    lookup_field = "slug_name"

    def get_queryset(self):
        """Get business queryset"""
        user = self.request.user

        if user.is_superuser or not user.is_authenticated:
            return Business.objects.all()
        return Business.objects.filter_by_members([user])

    def get_permissions(self):
        """Get permissions based on actions"""

        perms = []
        if self.action in ['retrieve']:
            perms.append(AllowAny)
        else:
            perms.extend([IsAdminOrBusinessMemberObject, CustomDjangoModelPermissions])
        return [permission() for permission in perms]

    def get_serializer_class(self):
        print(self.action)
        if self.action in ['update', 'partial_update']:
            return serializers.BusinessUpdateSerializer
        if self.action in ['retrieve', 'list']:
            if self.request.user.is_staff:
                return serializers.BusinessSerializer
            else:
                return serializers.BusinessPublicSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=True)
    def stats(self, request, *args, **kwargs):
        """Return business stats"""

        instance = self.get_object()
        serializer = serializers.BusinessStatsSerializer(instance)
        return Response(serializer.data)

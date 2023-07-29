"""Business views"""

# Django
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

# REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny
from core.business import permissions as business_perms
from core.utils.permissions import CustomDjangoModelPermissions

# Models
from core.events.models import Event
from core.business.models import Business

# Serializers
from core.events import serializers

# Utils
from core.utils.mixins import GetObjectSelectForUpdateMixin
from core.events import exceptions


class EventModelViewSet(GetObjectSelectForUpdateMixin,
                        viewsets.ModelViewSet):
    """
    ViewSet Model for viewing and editing event.
    """
    lookup_field = "uuid"
    pagination_class = None

    def dispatch(self, request, *args, **kwargs):
        business_slug_name = kwargs.get('business_slug_name')
        self.business = get_object_or_404(Business, slug_name=business_slug_name)

        return super().dispatch(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        """Get serializer based on user"""

        if self.request.user.is_staff:
            serializer_class = serializers.EventAdminSerializer
        else:
            serializer_class = serializers.EventPublicSerializer
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_permissions(self):
        """Get permissions based on actions"""

        perms = []
        if self.action in ['update', 'destroy']:
            perms.extend([business_perms.IsAdminOrBusinessMemberObject,
                         business_perms.IsAdminOrBusinessMember,
                         CustomDjangoModelPermissions])
        else:
            perms.append(AllowAny)
        return [permission() for permission in perms]

    def get_queryset(self):
        """Get event based on book"""

        queryset = Event.objects.filter_by_business(self.business)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = serializers.EventCreate(
            data=request.data,
            context={
                'business': self.business,
                'request': self.request
            }
        )

        serializer.is_valid(raise_exception=True)
        try:
            event = serializer.save()
        except IntegrityError:
            raise exceptions.ConflictSchedule(_("The event has schedule conflicts."))
        response_data = self.get_serializer(event).data

        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Update view"""

        partial = kwargs.pop('partial', False)
        instance = self.get_object(for_update=True)
        serializer = serializers.EventUpdate(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        event = serializer.save()
        response_data = self.get_serializer(event).data
        return Response(response_data, status=status.HTTP_201_CREATED)

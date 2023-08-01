"""Books views"""

# Django
from django.shortcuts import get_object_or_404

# REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny
from core.business import permissions as business_perms
from core.utils.permissions import CustomDjangoModelPermissions

# Models
from core.books.models import Book
from core.business.models import Business

# Serializers
from core.books import serializers

# Utils
from core.utils.mixins import GetObjectSelectForUpdateMixin


class BookModelViewSet(GetObjectSelectForUpdateMixin,
                       viewsets.ModelViewSet):
    """
    ViewSet Model for viewing and editing business.
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
            serializer_class = serializers.BookAdminSerializer
        else:
            serializer_class = serializers.BookPublicSerializer
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_permissions(self):
        """Get permissions based on actions"""

        perms = []
        if self.action in ['list']:
            perms.append(AllowAny)
        else:
            perms.extend([business_perms.IsAdminOrBusinessMemberObject,
                         business_perms.IsAdminOrBusinessMember,
                         CustomDjangoModelPermissions])
        return [permission() for permission in perms]

    def get_queryset(self):
        """Get book based on business."""

        queryset = Book.objects.filter_by_business(self.business)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = serializers.BookCreate(
            data=request.data,
            context={
                'business': self.business
            }
        )

        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        response_data = self.get_serializer(book).data

        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Update view"""

        partial = kwargs.pop('partial', False)
        instance = self.get_object(for_update=True)
        serializer = serializers.BookUpdate(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        book = serializer.save()
        response_data = self.get_serializer(book).data
        return Response(response_data, status=status.HTTP_200_OK)

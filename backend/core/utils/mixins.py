"""Utils mixins"""

# Django
from django.shortcuts import get_object_or_404


class GetObjectSelectForUpdateMixin:
    """Add get_object method with select_for_update"""

    def get_object(self, for_update=False):
        """Get object"""

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # pylint: disable = consider-using-f-string
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        if for_update:
            queryset = queryset.select_for_update()

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

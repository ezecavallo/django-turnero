"""Events filters"""

# Django-filters
from django_filters import (
    FilterSet,
    BooleanFilter,
    CharFilter
)

# Models
from core.events.models import Event


class EventFilterSet(FilterSet):
    """Filter for event"""
    query = CharFilter(method='get_query_type')
    month = BooleanFilter(field_name='published_on', method='filter_published')
    published = BooleanFilter(field_name='published_on', method='filter_published')

    def get_query_type(self, queryset, name, value):
        """Get query type"""
        # construct the full lookup expression.
        print(self.filters)
        if value == "month":
            return queryset.filter()

        # lookup = '__'.join([name, 'isnull'])

        # alternatively, you could opt to hardcode the lookup. e.g.,
        # return queryset.filter(published_on__isnull=False)

    class Meta:
        model = Event
        fields = ['query']

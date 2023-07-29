"""Companies urls."""

# Django
from django.urls import path, include

# REST Framework
from rest_framework import routers

# Views
from core.events import views

router = routers.SimpleRouter()
router.register(
    r'business/(?P<business_slug_name>[a-zA-Z0-9-_]+)/events',
    views.EventModelViewSet,
    basename="events"
)


urlpatterns = [
    # companies urls
    path('api/', include((router.urls, 'events')))
]

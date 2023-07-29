"""Books urls."""

# Django
from django.urls import path, include

# REST Framework
from rest_framework import routers

# Views
from core.books import views

router = routers.SimpleRouter()
router.register(
    r'business/(?P<business_slug_name>[a-zA-Z0-9-_]+)/books',
    views.BookModelViewSet,
    basename="books"
)


urlpatterns = [
    # books urls
    path('api/', include((router.urls, 'books')))
]

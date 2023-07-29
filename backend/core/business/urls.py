"""Business urls."""

# Django
from django.urls import path, include

# REST Framework
from rest_framework import routers

# Views
from core.business import views

router = routers.SimpleRouter()
router.register(r'business', views.BusinessModelViewSet, basename="business")


urlpatterns = [
    # business urls
    path('api/', include((router.urls, 'business')))
]

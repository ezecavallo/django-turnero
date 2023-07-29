"""Users urls."""

# Django
from django.urls import path, re_path, include

# REST Framework
from rest_framework.routers import SimpleRouter

# Views
from .views import (
    KnoxLoginView,
    KnoxRegisterView,
    KnoxLogoutView,
    GoogleLogin,
)
from dj_rest_auth.registration.views import VerifyEmailView

router = SimpleRouter()


urlpatterns = [
    # users urls

    # Google auth
    path('google/login/', GoogleLogin.as_view(), name='google_login'),

    # dj_rest_auth
    path('login/', KnoxLoginView.as_view(), name='knox_login'),
    path('registration/', KnoxRegisterView.as_view(), name='knox_register'),
    path('logout/', KnoxLogoutView.as_view(), name='knox_logout'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(r'^accounts/', include('allauth.urls')),
    re_path(
        r'^account-confirm-email/$',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$',
        VerifyEmailView.as_view(),
        name='account_confirm_email'
    ),
    # invoices urls
    path('api/', include(router.urls))
]

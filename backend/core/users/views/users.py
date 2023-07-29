"""Users views"""

# Django
from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

# REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# dj_rest_auth
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import SocialLoginView

# Knox
from knox.auth import TokenAuthentication


# Allauth
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from core.users.serializers import KnoxSerializer
from core.users.utils import create_knox_token


class CustomSocialLoginView(SocialLoginView):
    """Custom Social Login View"""

    def get_response(self):
        """get response"""
        serializer_class = self.get_response_serializer()
        data = {
            'user': self.user,
            'token': self.token
        }
        serializer = serializer_class(instance=data, context={'request': self.request})

        return Response(serializer.data, status=200)


class GoogleLogin(CustomSocialLoginView):
    """Google Login View"""
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:3000/login/google/'
    client_class = OAuth2Client


class KnoxLoginView(LoginView):
    """Knox Login View"""

    def get_response(self):
        """get response"""
        serializer_class = self.get_response_serializer()
        data = {
            'user': self.user,
            'token': self.token
        }
        serializer = serializer_class(instance=data, context={'request': self.request})

        return Response(serializer.data, status=200)


class KnoxLogoutView(LogoutView):
    """Knox Logout"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Define GET method not allowed"""
        self.http_method_not_allowed(request, *args, **kwargs)

    def logout(self, request):
        """logout"""
        try:
            request._auth.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response(
            {'detail': _('Successfully logged out.')},
            status=status.HTTP_200_OK,
        )

        return response


class KnoxRegisterView(RegisterView):
    """Know Registration View"""

    def get_response_data(self, user):
        return KnoxSerializer({'user': user, 'token': self.token}).data

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        self.token = create_knox_token(None, user, None)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return user

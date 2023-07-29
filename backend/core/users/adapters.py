from allauth.account.adapter import DefaultAccountAdapter


class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    """Overwrite DefaultAccountAdapter to prevent sessionid to be set"""

    def login(self, request, user):
        pass

    def get_login_redirect_url(self, request):
        return None

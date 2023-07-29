"""Main URLs module."""

# Django
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Users
    path('user/', include(('core.users.urls'), namespace='')),
    # path('accounts/', include('allauth.urls')),

    # subscriptions
    path('', include(('core.subscriptions.urls', 'subscriptions'), namespace='')),
    # business
    path('', include(('core.business.urls', 'business'), namespace='')),
    # books
    path('', include(('core.books.urls', 'books'), namespace='')),
    # events
    path('', include(('core.events.urls', 'events'), namespace='')),
    # transactions
    path('', include(('core.transactions.urls', 'transactions'), namespace='')),
    # MercadoPago
    path('', include(('core.mercadopago.urls', 'mp'), namespace='')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

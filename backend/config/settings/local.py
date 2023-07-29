"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='Generatearandomkeypls')
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "192.168.0.201",
    # Dev server
    "*",
]

# Admin
ADMIN_URL = 'admin/'

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_BACKEND = env(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend'
)
# EMAIL_HOST = env('DJANGO_EMAIL_HOST', default='localhost')
# EMAIL_PORT = env('DJANGO_EMAIL_PORT', default=1025)
# EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER', default='')
# EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD', default='')
# EMAIL_USE_TLS = True

# Celery
CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_EAGER_PROPAGATES = False

"""Base settings to build other settings files upon."""

import environ
from datetime import timedelta

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('core')

env = environ.Env()

# Base
DEBUG = env.bool('DJANGO_DEBUG', False)

LANGUAGE_CODE = 'es-ar'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Translations
LOCALE_PATHS = [
    str(APPS_DIR.path('locale'))
]

SITE_ID = 1

# Databases
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLs
ROOT_URLCONF = 'config.urls'

# WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Auth model
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
TOKEN_TTL = timedelta(days=10)


REST_SESSION_LOGIN = False
REST_AUTH_TOKEN_MODEL = 'knox.models.AuthToken'
REST_AUTH_TOKEN_CREATOR = 'core.users.utils.create_knox_token'
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'core.users.serializers.CustomRegisterSerializer',
}
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'core.users.serializers.CustomLoginSerializer',
    'USER_DETAILS_SERIALIZER': 'core.users.serializers.UserDetailsCustomSerializer',
    'TOKEN_SERIALIZER': 'core.users.serializers.KnoxSerializer',
}
# REST_AUTH_REGISTER_PERMISSION_CLASSES = ()

# AllAuth
ACCOUNT_ADAPTER = "core.users.adapters.DefaultAccountAdapterCustom"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "rest_framework.authtoken",
    'knox',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'generic_relations',
    'django_extensions',
    "django_filters",
    'simple_history',
]
LOCAL_APPS = [
    'core.users.apps.UsersAppConfig',
    'core.subscriptions.apps.SubscriptionsAppConfig',
    'core.business.apps.BusinessAppConfig',
    'core.books.apps.BooksAppConfig',
    'core.events.apps.EventsAppConfig',
    'core.mercadopago.apps.MercadoPagoAppConfig',
    'core.transactions.apps.TransactionsAppConfig',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

# Static files
STATIC_ROOT = str(APPS_DIR.path('staticfiles'))
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media
MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('template')),
            str(APPS_DIR.path('static/template')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Security
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_HTTPONLY = False
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
# SESSION_COOKIE_AGE =

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]
# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "origin",
#     "user-agent",
# ]

CORS_EXPOSE_HEADERS = [
    "content-disposition",
]

# Fixtures
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# Admin
ADMINS = [
]
MANAGERS = ADMINS

# Site
SITE_ID = 1

# Celery
INSTALLED_APPS += ['core.taskapp.celery.CeleryAppConfig']
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60

# REST Framework
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exceptions.django_error_handler',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.utils.pagination.StandardPageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

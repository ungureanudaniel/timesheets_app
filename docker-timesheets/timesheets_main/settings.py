from pathlib import Path
import os
from django.conf import settings
from dotenv import load_dotenv
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _

load_dotenv(verbose=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = []
if os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS.extend(os.getenv('ALLOWED_HOSTS').split(' '))

DEVELOPMENT = bool(os.environ.get("DEBUG", default=0))

# -----------authentication----------------------
AUTH_USER_MODEL = 'users.CustomUser'
AUTH_TOKEN_LENGTH = 100
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # message frmwk
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    # developer added libraries
    'django.contrib.sitemaps',
    'django.conf.urls.i18n',
    'hitcount',
    'django.contrib.sites',
    # 'django_recaptcha',
    # user apps
    'widget_tweaks',
    'general',
    'users',
    'timesheet',
    'reports',
    'api',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    "axes",
]


INTERNAL_IPS = [
    "127.0.0.1",
]


MIDDLEWARE = [
    # 'django.middleware.gzip.GZipMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # --------caching middleware------------------
    # --------whitenoise middleware for media load
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # --------django internalization for language selection
    'django.contrib.messages.middleware.MessageMiddleware',  # message frmwk
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    # --------caching middleware-------------------
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # -----------authentication---------------------
    'allauth.account.middleware.AccountMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'timesheets_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]


# Enable caching in project
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "memcached:11211",
    }
}
WSGI_APPLICATION = 'timesheets_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("POSTGRES_DB", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ro'  # Set the language code for Romanian

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LANGUAGES = (
    ('ro', _('Română')),
    ('en', _('English')),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
DEFAULT_LANGUAGE = 1

# ==============authentication settings=========================
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
}

# Whether email is required during signup
ACCOUNT_EMAIL_REQUIRED = True

# Whether email verification is mandatory before login
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Or 'optional', 'none'

# Disable username (optional)
ACCOUNT_USERNAME_REQUIRED = True

# Set unique email (one account per email)
ACCOUNT_UNIQUE_EMAIL = True

# Authentication method ('email' for email only, 'username' for username, 'username_email' for both)
ACCOUNT_AUTHENTICATION_METHOD = 'username'

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'  # Redirect after logout
# ==============EMAIL SETTINGS==========================
# -----test
if DEBUG:
    # --------development
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    # -----production
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# -----email credentials
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'contact@bucegipark.ro'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
ACCOUNTANT_EMAIL = os.getenv('ACCOUNTANT_EMAIL')
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ============ django-resized settings ====================
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_SCALE = 0.5
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'WebP'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'WebP': ".WebP"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
# ============ django-messages framework ====================
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# ==============recaptcha keys===============================
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_SECRET')
if os.getenv('DEVELOPMENT'):
    SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# ================django simple captcha======================
CAPTCHA_IMAGE_SIZE = (100, 50)
CAPTCHA_BACKGROUND_COLOR = "#2eb872"
CAPTCHA_FOREGROUND_COLOR = "black"
# ================django payments settings=====================
TICKET_EMAIL_HEADER = os.getenv('TICKET_EMAIL_HEADER')
BASE_URL = os.getenv('BASE_URL')
# =====================LOGGING  ERRORS=========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'pnb_main.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': False,
            'level': 'ERROR',
        },
        'services': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'payments': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

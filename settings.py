1# Django settings for simply project.

from path import path
import os
import sys
import logging

PROJECT_ROOT = path(__file__ ).dirname()
# SITE_ROOT = path(PROJECT_ROOT / '..').abspath()
SITE_ROOT = PROJECT_ROOT
sys.path.insert(0, str(SITE_ROOT))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# Absolute filesystem path to the directory that will hold site static assets
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# django-mediagenerate needs dev/prod or throws null error
MEDIA_URL = '/media/'

DEV_MEDIA_URL = STATIC_URL

# The main media directory for django-mediagenerator
GLOBAL_MEDIA_DIRS = (
    STATIC_ROOT,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# StaticFiles from django-mediagenerator
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '_generated_media'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&%+980ogy34kof+_k24lcw^b!&1c+b2s^@5^)9^f9ksy%q)qg('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'mediagenerator.middleware.MediaMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MEDIA_BUNDLES = (
    ('main.css',
     'css/normalize.css',
     'css/styles.css',),
    ('index.css',
      'css/animate.css',
      'css/mandala.css',),
    ('board.css',
      'css/innerboard.css',
      'css/colorbox.css',),
    ('shop.css',
      'css/shop.css',),

    ('libraries.js',
     'js/jquery-1.7.2.min.js',
     'js/jquery-ui.min.js',
     'js/jquery.pagescroller.lite.js',
     'js/scripts.js',),
    ('index.js',
     'js/jquery.color.js',),
    ('board.js',
     'js/innerboard.js',
     'js/jquery.colorbox-min.js',),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    # other vendor modules
    'mediagenerator',
    'storages',
    'bootstrap3',
    'south',
    
    # simply modules
    'main',
    'backend',
)

# we don't want django-mediagenerate to import apps images
IGNORE_APP_MEDIA_DIRS = INSTALLED_APPS

# where is the static coming from
# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

DEBUG = TEMPLATE_DEBUG = os.environ.get('DEBUG_MODE', False)
MEDIA_DEV_MODE = False

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = '7gportal'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'main.api.s3.MediaS3BotoStorage' 
STATICFILES_STORAGE = 'main.api.s3.StaticS3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
DEV_MEDIA_URL = PRODUCTION_MEDIA_URL = STATIC_URL = S3_URL

STATIC_URL = S3_URL + 'static/'
PRODUCTION_MEDIA_URL = STATIC_URL

try:
    from settings_local import *
except ImportError:
    pass


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TRAP_IT_ACCESS_INFO = {
    "auth_id": "bmcfarland@spling.com",
    "auth_secret": "Discover",
}

SPLING_COM_ACCESS_INFO = {
    'url': 'http://7gportal.spling.com/api/2',
    'username': 'NewSimplyCentered',
    'password': 'splingit!',
}
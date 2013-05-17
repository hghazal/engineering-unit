import os
import dj_database_url

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = False
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Django Errors GG', 'hghazal@leanin.com'),
)

MANAGERS = (
    ('Managers', 'hghazal@leanin.com'),
)

SITE_ID = 1

TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en-us'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'firjcb+$#(2=k!$b_aneveap&*#6j1qru&i*)pe&5+l-ysx^24'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newrelic.extras.framework_django',

    'home',
    'projects',
    'django.contrib.admin',

    'compressor',
    'gunicorn',
    'django_extensions',
    # 'south',
)

#==============================================================================
# Context Processors
#==============================================================================

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

DATABASES = {
    'default': dj_database_url.config(default='mysql://eu:enggunit@localhost/eu'),
}

#==============================================================================
# Project URLS and media settings
#==============================================================================

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'sitestatic')
STATIC_URL = '/sitestatic/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# django-compressor settings
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc --include-path={path} {{infile}} {{outfile}}'.format(path=STATIC_ROOT)),
    ('text/coffeescript', 'coffee --compile --stdio'),
)

COMPRESS_OUTPUT_DIR = ""
COMPRESS_OFFLINE = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_DEBUG_TOGGLE = 'nocompress'
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_ENABLED = True

#==============================================================================
# Templates
#==============================================================================

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

ROOT_URLCONF = 'eu.urls'

WSGI_APPLICATION = 'eu.wsgi.application'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = [
    '*',
]
#==============================================================================
# Loggingx
#==============================================================================
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_LOCATION = os.path.join(PROJECT_ROOT, "logs/django.log").replace("\\", "/")

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
        },
        'mainlog': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_LOCATION,
            # 'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['mainlog'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

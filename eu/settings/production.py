from .common import *


DEBUG = False

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://5a9af0b6ecab4e59a880ea6ebf4dfdfc:921878173e404be090f79dd4c521b01c@app.getsentry.com/8494',
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
)

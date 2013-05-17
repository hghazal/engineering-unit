import os

if 'DOMAIN' in os.environ:
    current_domain = os.environ['DOMAIN']
    if current_domain == 'prod':
        from .production import *
else:
    from .development import *

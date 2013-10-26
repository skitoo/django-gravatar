
from django.conf import settings

def configure_default_settings():
    settings.GRAVATAR_SECURE      = getattr(settings, 'GRAVATAR_SECURE', False)
    settings.GRAVATAR_DEFAULT_URL = getattr(settings, 'GRAVATAR_DEFAULT_URL', '')


from django.conf import settings

GRAVATAR_DEFAULT_URL = getattr(settings, 'GRAVATAR_DEFAULT_URL', '')

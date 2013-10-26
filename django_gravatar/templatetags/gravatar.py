
from django.template import Library
from django.conf import settings
from django_gravatar.settings import configure_default_settings

configure_default_settings()

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import hashlib

register = Library()


@register.simple_tag
def gravatar_url(email, size=80):
    url = 'http'
    if settings.GRAVATAR_SECURE:
        url += 's'
    url += '://www.gravatar.com/avatar/'  + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + '?'
    url += urlencode([
        ('s', str(size)),
        ('d', settings.GRAVATAR_DEFAULT_URL)
    ])
    return url


@register.simple_tag
def gravatar(email, size=80, options=""):
    url = gravatar_url(email, size)
    return '<img src="%s" width="%s" height="%s" %s >' % (url, size, size, options)


from django.template import Library
from django_gravatar.settings import GRAVATAR_DEFAULT_URL, GRAVATAR_SECURE

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import hashlib

register = Library()


@register.simple_tag
def gravatar_url(email, size=80):
    url = 'http'
    if GRAVATAR_SECURE:
        url += 's'
    url += '://www.gravatar.com/avatar/'  + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + '?'
    url += urlencode({'d': GRAVATAR_DEFAULT_URL, 's': str(size)})
    return url


@register.simple_tag
def gravatar(email, size=80, options=""):
    url = gravatar_url(email, size)
    return '<img src="%s" width="%s" height="%s" %s >' % (url, size, size, options)

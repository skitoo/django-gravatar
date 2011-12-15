
from django.template import Library
from django_gravatar.settings import GRAVATAR_DEFAULT_URL
import urllib, hashlib

register = Library()


@register.simple_tag
def gravatar_url(email, size=80):
    return "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?" + urllib.urlencode({'d':GRAVATAR_DEFAULT_URL, 's':str(size)})


@register.simple_tag
def gravatar(email, size=80, options=""):
    url = gravatar_url(email, size)
    return '<img src="%s" width="%s" height="%s" %s />'%(url, size, size, options)


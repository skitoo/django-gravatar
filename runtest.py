import os

from django.conf import settings
from django.core.management import call_command


if not settings.configured:
    settings.configure(
        ADMINS = (
            ('test@example.com', 'Mr. Test'),
        ),

        MEDIA_ROOT = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')),

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'gravatar.db',
                'TEST_NAME': 'gravatar-test.db',
            }
        },

        INSTALLED_APPS = [
            'django_gravatar',
        ],

        DEBUG = True,
        TEMPLATE_DEBUG = True,
        SECRET_KEY = 'verysecret',
    )

call_command('test', 'django_gravatar')

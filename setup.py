#!/usr/bin/env python

from setuptools import setup, find_packages
import django_gravatar, os


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author = 'Alexis Couronne',
    author_email = 'alexis.couronne@gmail.com',
    name = 'django-simple-gravatar',
    version = django_gravatar.__version__,
    description = 'Django Gravatar is a lightweight Django application that allows you to insert a Gravatar image in your templates.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords = 'django gravatar avatar',
    url = 'https://github.com/skitoo/django-gravatar',
    license = 'New BSD License',
    platforms = ['OS Independent'],
    classifiers = CLASSIFIERS,
    packages = find_packages() 
)

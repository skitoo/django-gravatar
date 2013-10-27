# -*- coding: utf-8 -*-

from django.test import TestCase
from .templatetags.gravatar import gravatar_url, gravatar


class TestGravatar(TestCase):
    def test_gravatar_url(self):
        self.assertEqual('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=', gravatar_url('alexis.couronne@gmail.com'))
        self.assertEqual('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=120&d=', gravatar_url('alexis.couronne@gmail.com', 120))

    def test_gavatar(self):
        html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=" width="80" height="80"  >'
        self.assertEqual(html, gravatar('alexis.couronne@gmail.com'))

        html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=130&d=" width="130" height="130"  >'
        self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 130))

        html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=180&d=" width="180" height="180" class="avatar" >'
        self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 180, 'class="avatar"'))


class TestGravatarWithSecureActivated(TestCase):
    def test_gravatar_url(self):
        with self.settings(GRAVATAR_SECURE=True):
            self.assertEqual('https://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=', gravatar_url('alexis.couronne@gmail.com'))
            self.assertEqual('https://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=120&d=', gravatar_url('alexis.couronne@gmail.com', 120))

    def test_gavatar(self):
        with self.settings(GRAVATAR_SECURE=True):
            html = '<img src="https://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=" width="80" height="80"  >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com'))

            html = '<img src="https://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=130&d=" width="130" height="130"  >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 130))

            html = '<img src="https://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=180&d=" width="180" height="180" class="avatar" >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 180, 'class="avatar"'))


class TestGravatarWithDefaultGravatarUrl(TestCase):
    def test_gravatar_url(self):
        with self.settings(GRAVATAR_DEFAULT_URL='www.foo.com'):
            self.assertEqual('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=www.foo.com', gravatar_url('alexis.couronne@gmail.com'))
            self.assertEqual('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=120&d=www.foo.com', gravatar_url('alexis.couronne@gmail.com', 120))

    def test_gavatar(self):
        with self.settings(GRAVATAR_DEFAULT_URL='www.foo.com'):
            html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=www.foo.com" width="80" height="80"  >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com'))

            html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=130&d=www.foo.com" width="130" height="130"  >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 130))

            html = '<img src="http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=180&d=www.foo.com" width="180" height="180" class="avatar" >'
            self.assertEqual(html, gravatar('alexis.couronne@gmail.com', 180, 'class="avatar"'))


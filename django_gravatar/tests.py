# -*- coding: utf-8 -*-

from django.utils import unittest
from .templatetags.gravatar import gravatar_url, gravatar


class TestGravatar(unittest.TestCase):
    def test_gravatar_url(self):
        self.assertEquals('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=80&d=', gravatar_url('alexis.couronne@gmail.com'))
        self.assertEquals('http://www.gravatar.com/avatar/d7935ea08d17e261d3b0d12c04759c9d?s=120&d=', gravatar_url('alexis.couronne@gmail.com', 120))

#!/usr/bin/env python

import os
import sys

from django.core.management import execute_manager
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import settings

if __name__ == "__main__":
    execute_manager(settings)

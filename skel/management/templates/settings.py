"""
settings.py -- Local site settings

Override in this what you wish.  By default it simply imports the
site default settings and overrides nothing.

This file should *not* be checked into git.
"""

import sys

from siteSettings import *

# Make this unique, and don't share it with anybody.  Used by Django's
# cookie-based authentication mechanism.
SECRET_KEY = '{{ secretKey }}'

# For example, override the database settings:
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'dev.db'
#    }
#}

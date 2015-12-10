# __BEGIN_LICENSE__
# Copyright (c) 2015, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# The xGDS platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# __END_LICENSE__

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

#
# NOTE: Configuration below is an example for a production server.  Uncomment and tune
#       for your production config as needed.  Note that the email backend line MUST be
#       uncommented for outgoing email to actually get sent.  By default it is just written
#       to a file in /tmp (see siteSettings.py).
#

# SERVER_ROOT_URL = 'https://basalt.xgds.org/'

# GEOCAM_UTIL_SECURITY_ENABLED = True
# GEOCAM_UTIL_SECURITY_SSL_REQUIRED_BY_DEFAULT = True
# GEOCAM_UTIL_SECURITY_REQUIRE_ENCRYPTED_PASSWORDS = True
# GEOCAM_UTIL_SECURITY_LOGIN_REQUIRED_BY_DEFAULT = True

# EMAIL_HOST="email.arc.nasa.gov"
# EMAIL_PORT=25
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# MANAGERS = (
#     # Addresses listed here will get notification when a new user requests an account
#     ('Darlene Lim', 'darline.lim@nasa.gov'),
#     ('Tamar Cohen', 'tamar.e.cohen@nasa.gov'),
#     ('Dave Lees', 'david.s.lees@nasa.gov'),
# )

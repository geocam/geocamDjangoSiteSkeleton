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

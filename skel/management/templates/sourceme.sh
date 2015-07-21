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

{% if virtualEnvDir %}
# Activate virtualenv environment
source {{ virtualEnvDir }}bin/activate
{% endif %}

# Set DJANGO_SCRIPT_NAME to the URL prefix for Django on your web server (with leading slash
# and trailing slash).  This setting is ignored if using the built-in Django development web
# server.
export DJANGO_SCRIPT_NAME='/'

# The auto-generated PYTHONPATH usually works, but you might need to add more directories
# depending on how you installed everything.
export PYTHONPATH={{ parentDir }}:{{ appsDir }}:$PYTHONPATH

# You should not need to change this.
export DJANGO_SETTINGS_MODULE='$$$$SITE_NAME$$$$.settings'

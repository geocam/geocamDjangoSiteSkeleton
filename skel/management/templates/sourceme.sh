{% if virtualEnvDir %}
# Activate virtualenv environment
source {{ virtualEnvDir }}bin/activate
{% endif %}

# Set DJANGO_SCRIPT_NAME to the URL prefix for Django on your web server (with leading slash
# and trailing slash).  This setting is ignored if using the built-in Django development web
# server.
export DJANGO_SCRIPT_NAME='/share/'

# The auto-generated PYTHONPATH usually works, but you might need to add more directories
# depending on how you installed everything.
export PYTHONPATH={{ parentDir }}:{{ appsDir }}:$PYTHONPATH

# You should not need to change this.
export DJANGO_SETTINGS_MODULE='$$$$SITE_NAME$$$$.settings'

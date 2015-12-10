#!/usr/bin/env python
#__BEGIN_LICENSE__
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
#__END_LICENSE__

import os
import sys

# pylint: disable=W0104

# try to bootstrap before hooking into django management stuff
if 'bootstrap' in sys.argv:
    extraArgs = sys.argv[2:]
else:
    extraArgs = []
ret = os.spawnl(os.P_WAIT, sys.executable, sys.executable, '%s/management/bootstrap.py' % os.path.dirname(__file__), *extraArgs)
if ret != 0 or extraArgs:
    sys.exit(ret)


try:
    from django.conf import settings
    settings.DATABASES  # force eval
except:
    if os.environ.get('SOURCED'):
        raise
    else:
        # may need to source sourceme.sh
        os.environ['SOURCED'] = '1'
        thisFile = os.path.realpath(__file__)
        parentDir = os.path.dirname(thisFile)
        ret = os.system('bash -c "(source %s/sourceme.sh && %s %s)"'
                        % (parentDir, thisFile, ' '.join(sys.argv[1:])))
        sys.exit(int(ret != 0))


try:
    import settings  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "$$$$SITE_NAME$$$$.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

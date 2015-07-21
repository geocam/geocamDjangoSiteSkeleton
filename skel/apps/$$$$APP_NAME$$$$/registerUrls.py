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

from django.conf.urls import patterns
from django.contrib import auth


urlpatterns = patterns('',
                       (r'^login/$', 'django.contrib.auth.views.login', {'loginRequired': False}, 'user-login'),
                       (r'^logout/$', 'django.contrib.auth.views.logout', {'loginRequired': False, 'next_page': '/accounts/login/'}),
                       (r'^register/$', 'basaltApp.register.registerUser', {'loginRequired': False}, 'user-registration'),
                       (r'^activate/(.*)$', 'basaltApp.register.activateUser', {}, 'user-activate'),
                       (r'^reset-password/$', auth.views.password_reset, {'loginRequired': False}, 'reset-password'),
                       (r'^reset-password-done/$', auth.views.password_reset_done, {'loginRequired': False}),
                       (r'^reset-password-confirm/(?P<uidb36>[^/]+)/(?P<token>.+)$', auth.views.password_reset_confirm, {'loginRequired': False}),
                       (r'^reset-password-complete/$', auth.views.password_reset_complete, {'loginRequired': False}),
                       )

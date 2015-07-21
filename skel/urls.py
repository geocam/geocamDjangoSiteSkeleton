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

from django.conf.urls import patterns, include
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib import auth
from django.views.generic import RedirectView, TemplateView

from django.contrib import admin
admin.autodiscover()

import $$$$APP_NAME$$$$.views

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^accounts/login/$', 'django.contrib.auth.views.login', {'loginRequired': False}, 'user-login'),
                       (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'loginRequired': False, 'next_page': '/accounts/login/'}),
                       (r'^accounts/register/$', '$$$$APP_NAME$$$$.register.registerUser', {'loginRequired': False}, 'user-registration'),
                       (r'^accounts/activate/(.*)$', '$$$$APP_NAME$$$$.register.activateUser', {}, 'user-activate'),
                       (r'^accounts/reset-password/$', auth.views.password_reset, {'loginRequired': False}, 'reset-password'),
                       (r'^accounts/reset-password-done/$', auth.views.password_reset_done, {'loginRequired': False}),
                       (r'^accounts/reset-password-confirm/(?P<uidb36>[^/]+)/(?P<token>.+)$', auth.views.password_reset_confirm, {'loginRequired': False}),
                       (r'^accounts/reset-password-complete/$', auth.views.password_reset_complete, {'loginRequired': False}),
                       (r'^$', RedirectView.as_view(url=settings.SCRIPT_NAME + '$$$$APP_NAME$$$$/'), {}),
                       (r'^$$$$APP_NAME$$$$/', include('$$$$APP_NAME$$$$.urls')),
                       (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + '$$$$APP_NAME$$$$/icons/favicon.ico'), {'readOnly': True}),
                       
                       # TODO uncomment as appropriate to include submodule urls
                       (r'^xgds_map_server/', include('xgds_map_server.urls')),
                       (r'^xgds_data/', include('xgds_data.urls')),
                       #  (r'^notes/', include('xgds_notes.urls')),
                       #  (r'^xgds_planner2/', include('xgds_planner2.urls')),
                       #  (r'^xgds_plot/', include('xgds_plot.urls')),
                       #  (r'^xgds_video/', include('xgds_video.urls')),
                       
                       )

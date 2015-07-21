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

import logging
from uuid import uuid4
import string

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.core import mail

from $$$$APP_NAME$$$$ import settings
from $$$$APP_NAME$$$$.forms import UserRegistrationForm

registration_email_template = string.Template(  # noqa
"""
Greetings, xGDS managers.

You have received a user registration request from xGDS PLRP from the user $username ($email).

$username says:
"$comments"

To activate this user, visit:
$url

The request came from $ip_address, and was referred by the form at $referrer
"""
)


def registerUser(request):
    if request.method not in ('GET', 'POST'):
        raise Exception("Invalid request method: " + request.method)
    # if request.user.is_authenticated:
    #    # Don't let them register again if they're already logged in.
    #    #return HttpResponseRedirect('/')
    #    return HttpResponse("You are already logged in.")
    if request.method == "GET":
        return render_to_response("registration/register.html",
                                  {'register_form': UserRegistrationForm()},
                                  context_instance=RequestContext(request))
    else:
        form = UserRegistrationForm(request.POST)

        if not form.is_valid():
            # FAIL
            logging.info("Create form validation failed.")
            return render_to_response("registration/register.html",
                                      {'register_form': form},
                                      context_instance=RequestContext(request))
        else:
            logging.info("Creating a new user")
            user_data = form.cleaned_data
            assert user_data.get('email')
            user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password1'])
            user.is_active = False
            user.save()
            mail.mail_managers(
                'Registration request from %s' % user.username,
                registration_email_template.substitute({
                    'username': user.username,
                    'email': user.email,
                    'url': request.build_absolute_uri(reverse('user-activate', args=[user.id])),
                    'comments': user_data['comments'],
                    'ip_address': request.META['REMOTE_ADDR'],
                    'referrer': request.META['HTTP_REFERER'],
                }),
            )
            return render_to_response("registration/simple_message.html",
                                      {'message': "You have successfully registered.  You will receive an email notification at %s after a site manager approves your request." % user.email},
                                      context_instance=RequestContext(request))


@permission_required('add_user')
def activateUser(request, user_id):

    def render_message(msg):
        return render_to_response("registration/simple_message.html",
                                  {'message': msg},
                                  context_instance=RequestContext(request))

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render_message("No user with the given id")

    if user.is_active:
        return render_message("The user %s has already been activated.  Someone must have gotten here first." % user.username)

    user.is_active = True
    user.save()
    mail.send_mail(
        settings.EMAIL_SUBJECT_PREFIX + "Your account has been activated",
        """
        Hi, $username.
        Your xGDS registration request has been approved.  Click to log in!
        $url
        """.substitute({'username': user.username,
                        'url': request.build_absolute_uri(reverse('user-login'))}),
        settings.SERVER_EMAIL,
        [user.email],
    )
    mail.mail_managers(
        settings.EMAIL_SUBJECT_PREFIX + "The user %s was activated." % user.username,
        """
        The User $username was successfully activated by $adminuser.
        """.substitute({'username': user.username,
                        'adminuser': request.user.username}),
    )
    return render_message("The user %s was successfully activated." % user.username)


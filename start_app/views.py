from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from init_django import utilities


def home( request ):

    context = {

    }

    utilities.get_messages( request, context )

    return render( request, 'home.html', context )
from django.shortcuts import render

import init_django.utilities as utilities

def home( request ):

    context = {

    }

    utilities.get_message( request, context )

    return render( request, 'home.html', context )
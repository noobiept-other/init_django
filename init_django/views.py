from django.shortcuts import render

def get_message( request, context ):

    """
        Checks the session to see if there's a message, and if so adds to the context object (don't forget, it changes the object from where its called)
    """

    message = request.session.get( 'message' )

    if message:

        context[ 'message' ] = message
        del request.session[ 'message' ]


def home( request ):

    context = {

    }

    get_message( request, context )

    return render( request, 'home.html', context )
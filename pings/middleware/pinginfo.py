from pings .models import Ping

class TrackPingMiddleware(object):
    #TODO edit/delete
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request BEFORE
        # the view (and later middleware) are called.

        # current_ping = response.get['ping']
        # if radio button selected:
            # ping = ping where pk = radio button selected one

        response = self.get_response(request)

        # Code to be executed for each request/response AFTER
        # the view is called.
        #print('Middleware executed')

        return response

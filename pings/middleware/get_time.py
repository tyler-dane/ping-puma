from datetime import datetime

class GetTimeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request BEFORE
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response AFTER
        # the view is called.
        # print('time now:', datetime.now())

        return response

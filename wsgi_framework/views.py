from .response import HTTPResponseNotAllowed, HTTPResponseNotFound


class BaseView:
    https_allowed_methods = ['get', 'post']

    def __init__(self, request):
        self.request = request

    def handle(self):
        if self.request.get('method') in self.https_allowed_methods:
            handler = getattr(self, self.request.get('method'), HTTPResponseNotAllowed()())  # ugly
            return handler(self.request)
        else:
            return HTTPResponseNotAllowed()()  # ugly


class NotFoundView(BaseView):
    def __init__(self, request):
        super(NotFoundView, self).__init__(request)
        self.request = request

    def handle(self):
        return HTTPResponseNotFound()()  # ugly

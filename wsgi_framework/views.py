from .response import HTTPResponseNotAllowed, HTTPResponseNotFound


class BaseView:
    https_allowed_methods = ['get', 'post']

    def __call__(self, request):
        if request.get('method') in self.https_allowed_methods:
            handler = getattr(self, request.get('method'), HTTPResponseNotAllowed()())  # ugly
            return handler(request)
        else:
            return HTTPResponseNotAllowed()()  # ugly


class NotFoundView(BaseView):
    def __call__(self, request):
        return HTTPResponseNotFound()()  # ugly

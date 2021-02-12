from .views import NotFoundView
from .middleware import MobileRefererMiddleware


class Application:
    urls = None
    middlewares = [
        MobileRefererMiddleware()
    ]

    def __call__(self, environ, start_response):
        view = self.urls.get(environ['PATH_INFO'], NotFoundView())
        request = {}

        # apply all middlewares
        for middleware in self.middlewares:
            middleware(environ, request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

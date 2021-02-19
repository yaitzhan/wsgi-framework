from .views import NotFoundView
from .middleware import MobileRefererMiddleware


class Application:
    urls = None
    middlewares = [
        MobileRefererMiddleware()
    ]

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path += '/'

        view = self.urls.get(path, NotFoundView())
        request = self.setup_request(environ)

        print('REQUEST:', request)  # for debug

        # apply all middlewares
        for middleware in self.middlewares:
            middleware(environ, request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

    def setup_request(self, environ):
        request = {
            'method': environ['REQUEST_METHOD'],
        }

        return request

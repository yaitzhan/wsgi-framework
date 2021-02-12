from .views import NotFoundView


class Application:
    urls = None

    def __call__(self, environ, start_response):
        view = self.urls.get(environ['PATH_INFO'], NotFoundView())
        request = {}
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

from views import SimpleView, NotFoundView

urls = {
    '/': SimpleView()
}


class Application:
    def __call__(self, environ, start_response):
        view = urls.get(environ['PATH_INFO'], NotFoundView())
        request = {}
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body




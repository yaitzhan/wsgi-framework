import json

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
            'body': self.body(environ),  # parse POST body data
            'query_params': self.get_query_params(environ)  # parse GET query params
        }

        return request

    def body(self, environ):
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ.get('wsgi.input').read(content_length) if content_length > 0 else b''
        if data:
            return json.loads(data.decode(encoding='utf-8').strip())
        return {}

    def get_query_params(self, environ):
        query_params_str = environ.get('QUERY_STRING')
        if query_params_str:
            result = {}
            for each in query_params_str.split('&'):
                k, v = each.split('=')
                result[k] = v
            return result

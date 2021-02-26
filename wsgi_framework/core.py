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

        request = self.setup_request(environ)
        view_cls = self.urls.get(path, NotFoundView)  # get the defined in urls.py view-class

        print('REQUEST:', request)  # for debug

        # apply all middlewares
        for middleware in self.middlewares:
            middleware(environ, request)
        view = view_cls(request)  # initialize view class passing request
        code, body = view.handle()
        start_response(code, [('Content-Type', 'text/html')])
        return body

    def setup_request(self, environ):
        request = {
            'method': environ['REQUEST_METHOD'].lower(),
            'body': self.body(environ),  # parse POST body data
            'query_params': self.get_query_params(environ)  # parse GET query params
        }

        return request

    def body(self, environ):
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ.get('wsgi.input').read(content_length) if content_length > 0 else b''
        if data:
            data = data.decode(encoding='utf-8')
            result = {}
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
            return result
        return {}

    def get_query_params(self, environ):
        query_params_str = environ.get('QUERY_STRING')
        if query_params_str:
            result = {}
            for each in query_params_str.split('&'):
                k, v = each.split('=')
                result[k] = v
            return result

class BaseView:
    return_code = None
    body = None

    def __call__(self, request):
        return self.return_code, self.body


class SimpleView(BaseView):
    return_code = '200 OK'
    body = [b'<h1>Simple View Example</h1>']


class NotFoundView(BaseView):
    return_code = '404 Not Found'
    body = [b'<h1>Not Found View Example</h1>']

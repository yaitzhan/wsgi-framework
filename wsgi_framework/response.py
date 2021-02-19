from http.client import responses


class HTTPResponse:
    status_code = 200

    def __init__(self, content='', reason=None):
        self._content = content
        self._reason = reason

    def __call__(self, *args, **kwargs):
        return '{} {}'.format(self.status_code, self.reason), self.content

    @property
    def reason(self):
        if self._reason is None:
            return responses.get(self.status_code, 'Unknown Status Code')
        return self._reason

    @property
    def content(self):
        return [self._content.encode(encoding='utf-8')]

    @content.setter
    def content(self, value):
        self._content = value


class HTTPResponseNotAllowed(HTTPResponse):
    status_code = 405


class HTTPResponseNotFound(HTTPResponse):
    status_code = 404


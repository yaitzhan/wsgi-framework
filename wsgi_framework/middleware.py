import re


class MobileRefererMiddleware:
    """
    Middleware для отслеживания зашел ли пользователь с мобильного устройства
    """
    def __call__(self, environ, request):
        user_agent = environ['HTTP_USER_AGENT']
        if re.search('mobile', user_agent, flags=re.I):
            request['mobile'] = True
        else:
            request['mobile'] = False


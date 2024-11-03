from django.utils.deprecation import MiddlewareMixin

class ThemeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        theme = request.COOKIES.get('theme', 'light')
        request.theme = theme

    def process_response(self, request, response):
        response.set_cookie('theme', request.theme)
        return response

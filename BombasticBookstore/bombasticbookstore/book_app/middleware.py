from django.utils.deprecation import MiddlewareMixin

class ThemeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        theme = request.COOKIES.get('theme', 'light')
        request.theme = theme
        print(f"Request theme: {theme}")  # Debugging

    def process_response(self, request, response):
        response.set_cookie('theme', request.theme)
        print(f"Response theme: {request.theme}")  # Debugging
        return response

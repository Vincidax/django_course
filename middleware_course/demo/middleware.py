


# middleware.py

class SimpleLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 👇 Code before the view (process request)
        print(f"User IP: {request.META.get('REMOTE_ADDR')}")

        response = self.get_response(request)

        # 👇 Code after the view (process response)
        print("Response status code:", response.status_code)

        return response

import logging
from datetime import datetime, time
from django.http import JsonResponse

logger = logging.getLogger('request_logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('requests.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        user_str = user.username if user and user.is_authenticated else 'Anonymous'

        logger.info(f"{datetime.now()} - User: {user_str} - Path: {request.path}")

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Define allowed access hours
        self.start_time = time(6, 0)   # 6:00 AM
        self.end_time = time(21, 0)    # 9:00 PM

    def __call__(self, request):
        now = datetime.now().time()

        # Check if current time is outside allowed range
        # Allowed: between 6 AM (inclusive) and 9 PM (exclusive)
        if not (self.start_time <= now < self.end_time):
            return JsonResponse(
                {"detail": "Access to messaging app is restricted between 9 PM and 6 AM."},
                status=403
            )

        response = self.get_response(request)
        return response
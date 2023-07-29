"""utils exceptions"""

from django.core.exceptions import ValidationError

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def django_error_handler(exc, context):
    """Handle django core's errors."""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is None and isinstance(exc, ValidationError):
        if isinstance(exc.messages, dict):
            data = exc.message_dict
        else:
            data = {'error': exc.messages}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
    return response

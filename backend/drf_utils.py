"""
Sometimes in your Django model you want to raise a ``ValidationError`` in the
``save`` method, for
some reason.
This exception is not managed by Django Rest Framework because it occurs after its
validation process. So at the end, you'll have a 500.
Correcting this is as simple as overriding the exception handler, by converting the
Django ``ValidationError`` to a DRF one.
"""

from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    """Handle Django ValidationError as an accepted exception

    Must be set in settings:

    >>> REST_FRAMEWORK = {
    ...     # ...
    ...     'EXCEPTION_HANDLER': 'drf_utils.exception_handler',
    ...     # ...
    ... }

    For the parameters, see ``exception_handler``

    """

    if isinstance(exc, DjangoValidationError):
        if hasattr(exc, 'message_dict'):
            exc = DRFValidationError(detail=exc.message_dict)
        else:
            exc = DRFValidationError(detail={'detail': exc.message})

    return drf_exception_handler(exc, context)

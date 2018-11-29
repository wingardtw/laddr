import datetime
from django.utils import timezone
from backend.settings import DEFAULT_MATCH_DURATION


def default_match_expire():
    return timezone.now() + datetime.timedelta(days=DEFAULT_MATCH_DURATION)

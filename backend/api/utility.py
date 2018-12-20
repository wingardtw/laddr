from backend.settings import DEFAULT_MATCH_DURATION
from django.utils import timezone
import datetime


def default_match_expire():
    return timezone.now() + datetime.timedelta(days=DEFAULT_MATCH_DURATION)

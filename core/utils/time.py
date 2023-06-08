from datetime import datetime

from django.utils import timezone


def get_now() -> datetime:
    """
    Returns the current datetime in the timezone set in Django's settings.
    """
    return timezone.now()


def timestamp_to_datetime(tms_tmp: int) -> datetime:
    """
    Converts a Unix timestamp to a datetime object in the timezone set in Django's settings.
    """
    return timezone.make_aware(datetime.fromtimestamp(tms_tmp))

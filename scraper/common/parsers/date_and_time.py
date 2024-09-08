import datetime
import logging
from typing import Optional

from scraper.common.types.date_and_time import DateAndTime


def parse_date_and_time(
    date_string: str,
    time_string: str,
) -> Optional[DateAndTime]:
    """Parse and combine the given date and time

    Both arguments should be in ISO-8601 format. The time should include the UTC offset.

    If the time cannot be parsed, use a time of 12:00 UTC.
    If the date cannot be parsed, return None.
    """
    logger = logging.getLogger(__name__)
    try:
        date = datetime.date.fromisoformat(date_string)
    except (TypeError, ValueError):
        logger.debug("Failed to parse date %r", date_string)
        return None

    time: Optional[datetime.time] = None
    try:
        time = datetime.time.fromisoformat(time_string)
    except (TypeError, ValueError):
        logger.debug("Failed to parse time %r", time)

    return DateAndTime(date=date, time=time)
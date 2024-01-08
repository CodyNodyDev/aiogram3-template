from datetime import datetime, date, timezone
from typing import Optional


async def get_date_time() -> Optional[str]:
    """
    :return: string with date and time ->  09/01/2024##19:22
    """

    current_date = date.today().strftime("%d/%m/%Y")
    hour = datetime.utcnow().replace(tzinfo=timezone.utc).hour
    minute = datetime.utcnow().replace(tzinfo=timezone.utc).minute

    date_time_data = f'{current_date}##{hour}:{minute}'
    return date_time_data

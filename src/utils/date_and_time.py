from datetime import datetime, date, timezone


async def get_date_time():
    current_date = date.today().strftime("%d/%m/%Y")
    hour = datetime.utcnow().replace(tzinfo=timezone.utc).hour
    minute = datetime.utcnow().replace(tzinfo=timezone.utc).minute

    date_time_data = f'{current_date}##{hour}:{minute}'
    return date_time_data

from datetime import datetime
import requests

def str_to_timestamp(hour: str, minute: str) -> datetime:
    now = datetime.now()
    new_now = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
    return new_now

async def get_timezones():
    timezones_list = requests.get("http://worldtimeapi.org/api/timezone")
    if timezones_list.ok:
        return timezones_list.json()
    else:
        return None
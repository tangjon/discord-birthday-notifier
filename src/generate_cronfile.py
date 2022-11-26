import pytz
from datetime import datetime


def is_dst(dt=None, timezone="UTC"):
    if dt is None:
        dt = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0


def generate_cron_tab():
    local_time_diff_from_utc = 7 if is_dst() else 8
    content = f"0 {local_time_diff_from_utc} * * * python /usr/src/app/src/main.py >> logfile.txt"
    with open("../crontab", "w") as f:
        f.write(content + "\n")

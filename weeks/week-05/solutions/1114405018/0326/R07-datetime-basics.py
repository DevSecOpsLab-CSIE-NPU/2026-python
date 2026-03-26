# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)  # 2
print(c.total_seconds() / 3600)  # 58.5

dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年自動處理
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    if start is None:
        start = datetime.today()
    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24

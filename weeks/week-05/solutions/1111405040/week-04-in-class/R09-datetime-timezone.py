"""
R09: 時區與 aware datetime。

示範重點：
1. 用 `ZoneInfo` 建立帶時區的 datetime。
2. 在不改變實際時間點的前提下轉換時區。
3. 查詢可用時區名稱。
"""

from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 帶 `tzinfo` 的 datetime 稱為 aware datetime，
# 它知道自己屬於哪個時區。
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# `astimezone()` 會把同一個時間點轉成另一個時區的顯示方式。
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 實務上常先轉成 UTC 再做儲存或跨系統交換。
now_utc = datetime.now(tz=utc)
print(now_utc)

# 這裡示範從 UTC 轉回美國中部時區。
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# `available_timezones()` 可列出環境中可用的時區名稱。
tw_zones = [zone_name for zone_name in available_timezones() if "Taipei" in zone_name]
print(tw_zones)  # ['Asia/Taipei']

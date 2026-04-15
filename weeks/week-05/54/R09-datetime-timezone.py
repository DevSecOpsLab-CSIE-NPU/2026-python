# R09. 時區操作（3.16）
# zoneinfo（Python 3.9+）取代 pytz

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# 轉換時區
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部用 UTC，輸出再轉本地
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢國家時區

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

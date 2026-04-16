"""R09 時區操作（3.16）。"""

# zoneinfo 是 Python 3.9+ 內建的時區工具，建議取代第三方 pytz

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime（aware datetime）
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# astimezone() 會保留同一瞬間，只改變顯示時區
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 內部資料建議用 UTC 儲存與計算
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部用 UTC，輸出時再轉成本地時區
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# available_timezones() 可列出系統可用時區名稱

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

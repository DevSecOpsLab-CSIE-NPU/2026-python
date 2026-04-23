# R09. 時區操作（3.16）
# zoneinfo（Python 3.9+）取代 pytz

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶有時區資訊的 datetime
# tzinfo 決定這個時間所屬的時區

d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# 使用 astimezone() 轉換成其他時區的本地時間
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得目前 UTC 時間
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：系統內部使用 UTC 儲存，輸出時再轉成本地時區
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢可用時區清單，並篩選出包含 Taipei 的項目

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

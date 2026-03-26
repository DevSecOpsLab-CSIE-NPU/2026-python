# R09. 時區操作（3.16）
#
# 這份範例說明如何使用 zoneinfo 處理「有時區」的 datetime：
# 1. 建立帶時區資訊的時間
# 2. 在不同時區之間做正確轉換
# 3. 掌握 UTC 與本地時間之間的最佳實務
#
# zoneinfo 是 Python 3.9+ 的標準做法，通常可取代舊式的 pytz 用法。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 先建立常用時區物件，後續重複使用時較清楚。
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime。
# tzinfo=central 表示這個時間是「芝加哥當地時間 2012-12-21 09:30」。
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# astimezone() 會保留「同一個實際時間點」，只改成目標時區的顯示方式。
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得目前 UTC 時間。
# 在系統內部統一使用 UTC，能降低跨時區與夏令時間造成的錯誤。
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部儲存與計算用 UTC，需要顯示給使用者時再轉成本地時區。
# 這個例子也示範了夏令時間切換附近的轉換行為。
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# available_timezones() 可列出系統可用的 IANA 時區名稱。
# 這裡示範簡單篩選出和 Taipei 有關的時區識別字串。
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

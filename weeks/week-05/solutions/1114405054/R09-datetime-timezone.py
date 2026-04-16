# R09. 時區操作（3.16）
# zoneinfo（Python 3.9+）取代 pytz

# datetime 用來建立日期時間，timedelta 可表示時間差
from datetime import datetime, timedelta
# ZoneInfo 用來建立時區物件，available_timezones() 可列出系統可用時區
from zoneinfo import ZoneInfo, available_timezones

# 先建立常用時區物件，後續可重複使用
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime
# tzinfo 參數可讓 datetime 直接成為「有時區資訊」的時間
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# 轉換時區
# astimezone() 會把同一個時間點轉換成另一個時區的當地時間
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間
# 建議在需要跨地區處理時，優先使用 UTC 當作標準時間
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部用 UTC，輸出再轉本地
# 先以 UTC 儲存或運算，顯示給使用者時再轉為目標時區
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢國家時區
# available_timezones() 會回傳可用時區名稱集合，這裡用字串篩選出台北相關時區
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

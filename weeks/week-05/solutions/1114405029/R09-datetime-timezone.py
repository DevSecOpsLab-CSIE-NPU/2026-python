# R09. 時區操作（3.16）
# 說明：zoneinfo（Python 3.9+）取代 pytz

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 建立時區物件
# UTC：世界協調時間
utc = ZoneInfo("UTC")

# 美國芝加哥中央標準時間（CST）
central = ZoneInfo("America/Chicago")

# 台北標準時間（CST，UTC+8）
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime
# 2012年12月21日 早上9:30，芝加哥時間
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 輸出：2012-12-21 09:30:00-06:00
# 注意：-06:00 表示芝加哥比 UTC 慢 6 小時

# 轉換時區
# 轉換為印度加爾各答時間（UTC+5:30）
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 輸出：2012-12-21 21:00:00+05:30

# 轉換為台北時間（UTC+8）
print(d.astimezone(taipei))  # 輸出：2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間
# now() 取得現在時間，tz=utc 指定時區
now_utc = datetime.now(tz=utc)
print(now_utc)

# ─────────────────────────────────────────────────────────────────
# 最佳實踐：內部用 UTC，輸出再轉本地
# 說明：儲存資料時使用 UTC，顯示時再轉換為當地時區
# ─────────────────────────────────────────────────────────────────

# 建立 UTC 時間
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
# 轉換為芝加哥時間（冬令時，UTC-6）
print(utc_dt.astimezone(central))  # 輸出：2013-03-10 01:45:00-06:00

# ─────────────────────────────────────────────────────────────────
# 查詢國家時區
# 說明：available_timezones() 取得所有可用時區
# ─────────────────────────────────────────────────────────────────

# 找出所有與台北相關的時區
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # 輸出：['Asia/Taipei']
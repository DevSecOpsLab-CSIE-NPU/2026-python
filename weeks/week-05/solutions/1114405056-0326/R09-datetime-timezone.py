from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# ── 建立時區物件 ──────────────────────────────────────────
# zoneinfo 是 Python 3.9+ 內建的時區庫，使用 IANA 時區資料庫名稱
utc = ZoneInfo("UTC")                  # 世界協調時間
central = ZoneInfo("America/Chicago")  # 美國中部時間（CST/CDT）
taipei = ZoneInfo("Asia/Taipei")       # 台北時間（UTC+8）

# ── 建立帶時區的 datetime（aware datetime）────────────────
# tzinfo 參數指定時區，建立後該物件即為 aware（有時區資訊）
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00（冬令 CST = UTC-6）

# ── 時區轉換：astimezone() ────────────────────────────────
# astimezone() 將同一個時刻轉換為不同時區的表示
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 印度標準時間 IST（UTC+5:30）
print(d.astimezone(taipei))                   # 台北時間（UTC+8）

# ── 取得當前 UTC 時間 ─────────────────────────────────────
# 永遠使用有時區的 datetime.now(tz=...) 而非 naive 的 datetime.now()
now_utc = datetime.now(tz=utc)
print(now_utc)

# ── UTC 轉當地時間 ────────────────────────────────────────
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
# 3/10 是美國夏令時間切換日，CDT = UTC-5
print(utc_dt.astimezone(central))

# ── 查詢包含 'Taipei' 的所有時區名稱 ─────────────────────
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

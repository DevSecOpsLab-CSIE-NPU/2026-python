# R09. 時區操作（3.16）
# 主題：zoneinfo（Python 3.9+）建立時區時間、轉換時區、最佳實務

from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

# ------------------------------------------------------------
# 一、建立常用時區物件
# ------------------------------------------------------------
# 建議使用 IANA 時區名稱（例如 Asia/Taipei, America/Chicago）
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# ------------------------------------------------------------
# 二、建立「帶時區」的 datetime
# ------------------------------------------------------------
# tzinfo 一旦存在，這個 datetime 就是 aware datetime（有時區語意）
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# ------------------------------------------------------------
# 三、跨時區轉換
# ------------------------------------------------------------
# astimezone() 會把同一個「絕對時間點」轉成目標時區顯示
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # +05:30
print(d.astimezone(taipei))                     # +08:00

# 取得目前 UTC 時間（建議後端儲存用 UTC）
now_utc = datetime.now(tz=utc)
print(now_utc)

# ------------------------------------------------------------
# 四、最佳實務
# ------------------------------------------------------------
# 內部資料統一存 UTC，輸出到前端/報表時再轉當地時區。
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))

# ------------------------------------------------------------
# 五、查詢可用時區
# ------------------------------------------------------------
# available_timezones() 回傳系統可用時區集合
# 這裡篩選出包含 Taipei 的項目。
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

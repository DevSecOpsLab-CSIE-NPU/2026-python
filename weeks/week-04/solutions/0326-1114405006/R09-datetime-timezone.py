# R09. 時區操作（3.16）
#
# 本檔案示範 Python 3.9+ 的 zoneinfo 時區處理方式：
# 1) 建立帶時區資訊的 datetime（aware datetime）
# 2) 在不同時區間做轉換
# 3) 使用 UTC 作為系統內部標準時間
# 4) 查詢可用時區清單
#
# 補充觀念：
# - naive datetime：沒有時區資訊（tzinfo=None）
# - aware datetime：有時區資訊（tzinfo=某個時區）
# - 實務上建議：內部儲存/計算用 UTC，展示時再轉在地時區

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 建立常用時區物件（IANA 時區名稱）
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime
# 這是 aware datetime：2012-12-21 09:30:00（芝加哥時間）
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# 轉換時區
# astimezone() 會保持「同一個絕對時間點」，只改用目標時區顯示
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間
# 使用 datetime.now(tz=utc) 可直接取得帶 UTC 時區的目前時間
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部用 UTC，輸出再轉本地
# 以下範例是 UTC 時間點，轉成 central 後會自動套用當地時區規則
# （包含是否為夏令時間 DST 的偏移計算）
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢國家時區
# available_timezones() 回傳系統可用的 IANA 時區名稱集合
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']

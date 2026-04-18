from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# ── 夏令時間切換的陷阱 ────────────────────────────────────
# 2013-03-10 凌晨 2:00 是美國夏令時間切換點（CST→CDT，時鐘撥快 1 小時）
# 1:45 AM CST 加 30 分鐘「看起來」是 2:15 AM，但這個時刻不存在！
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# ❌ 錯誤做法：直接對本地時間加 timedelta
# Python 不會自動調整夏令時鐘，導致結果在時區轉換時出錯
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15 AM CST（該時刻實際上不存在）

# ✅ 正確做法：先轉 UTC → 加減 → 再轉回本地時間
# UTC 不受夏令時間影響，算術運算永遠正確
utc_dt = local_dt.astimezone(utc)          # 轉為 UTC
correct = utc_dt + timedelta(minutes=30)   # 在 UTC 下加 30 分鐘
print(f"正確結果：{correct.astimezone(central)}")  # 自動轉換為 CDT

# ── 處理使用者輸入的 naive datetime ──────────────────────
# strptime 解析出來的 datetime 是 naive（無時區資訊）
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# replace(tzinfo=...) 指定時區（假設使用者在 Chicago 輸入）
# astimezone(utc) 轉換為 UTC 後存入資料庫（推薦做法）
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")
# 顯示時依使用者地區再轉回當地時間
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

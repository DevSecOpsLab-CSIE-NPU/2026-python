# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 說明：為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 建立時區物件
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# ─────────────────────────────────────────────────────────────────
# 問題：直接在本地時間加减，夏令時邊界會出錯
# 說明：美國夏令時開始時，時鐘會從凌晨 2:00 往前撥到 3:00
# 這會導致某些本地時間是不存在的
# ─────────────────────────────────────────────────────────────────

# 美國 2013-03-10 凌晨 1:45（夏令時開始前一小時）
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 直接加 30 分鐘會得到「不存在」的時間！
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 輸出：2:15（這個時間在夏令時切換時不存在！）


# ─────────────────────────────────────────────────────────────────
# 正確做法：先轉 UTC 計算，再轉回本地
# 說明：UTC 沒有夏令時問題，計算後再轉回當地時區
# ─────────────────────────────────────────────────────────────────

# 先將本地時間轉換為 UTC
utc_dt = local_dt.astimezone(utc)

# 在 UTC 中進行時間運算
correct = utc_dt + timedelta(minutes=30)

# 最後再轉回本地時區
print(f"正確結果：{correct.astimezone(central)}")  # 輸出：3:15（正確跳過了 2:xx）


# ─────────────────────────────────────────────────────────────────
# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 說明：儲存資料時使用 UTC，顯示時再轉換為當地時區
# ─────────────────────────────────────────────────────────────────

# 使用者輸入的時間字串（假設是芝加哥本地時間）
user_input = "2012-12-21 09:30:00"

# 1. 解析為無時區的 datetime
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# 2. 加上芝加哥時區，再轉換為 UTC 儲存
aware = naive.replace(tzinfo=central).astimezone(utc)

# 3. 輸出時轉為台北時區
print(f"存 UTC：{aware}")  # 輸出：2012-12-21 15:30:00+00:00
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")  # 輸出：2012-12-21 23:30:00+08:00
# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 本程式示範時區處理的最佳實踐：
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC
# 最佳實踐：輸入→UTC→計算→輸出時轉本地

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 定義時區
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")  # 中部時區（有夏令時）

# ── 夏令時跳躍問題示範 ──────────────────────────────
# 美國中部時區 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
# 這意味著 2:00-3:00 這個小時不存在

local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 錯誤做法：直接在本地時間加 30 分鐘
# 結果會落在不存在的 2:15
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！）

# 正確做法：先轉 UTC 計算，再轉回本地
utc_dt = local_dt.astimezone(utc)  # 轉為 UTC
correct = utc_dt + timedelta(minutes=30)  # 在 UTC 上加時間
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# ── 最佳實踐：UTC 優先工作流程 ─────────────────────
# 1. 輸入時間轉為 UTC 儲存
# 2. 所有計算都在 UTC 進行
# 3. 輸出時才轉為本地時間顯示

# 模擬使用者輸入（無時區資訊）
user_input = "2012-12-21 09:30:00"

# 解析為 naive datetime（無時區）
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# 假設輸入是本地時間（中部時區），轉為 aware datetime 再轉 UTC
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")

# 顯示時轉為台北時間
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

# ── 為什麼 UTC 優先？ ───────────────────────────────
# 1. UTC 沒有夏令時，不會有跳躍問題
# 2. 所有計算都在同一個時間軸上，避免歧義
# 3. 資料庫和 API 通常使用 UTC
# 4. 容易轉換到任何時區顯示

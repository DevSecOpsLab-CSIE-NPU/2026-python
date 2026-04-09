from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 定義時區物件
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago") # 美國中部時間（有夏令時 DST）

# --- 情境一：為什麼直接在本地時間做運算很危險？ ---
# 美國 2013-03-10 凌晨 2:00 時鐘會往前撥一小時（跳過 2 點，直接變成 3 點）
# 我們設定一個接近跳轉點的時間：1:45 AM
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 錯誤示範：直接對帶有本地時區的物件加 30 分鐘
wrong = local_dt + timedelta(minutes=30)
# 結果會是 2:15，但在該時區當天，2:15 是不存在的時間點（牆上時鐘直接從 1:59 跳到 3:00）
print(f"錯誤結果：{wrong}")  

# --- 正確做法：跨時區運算的標準流程 ---
# 1. 先將本地時間轉為 UTC
utc_dt = local_dt.astimezone(utc)
# 2. 在 UTC 環境下進行時間加減（UTC 永遠是線性的，沒有夏令時問題）
correct_utc = utc_dt + timedelta(minutes=30)
# 3. 計算完畢後，再轉回目標本地時區
print(f"正確結果：{correct_utc.astimezone(central)}")  # 顯示 3:15（這才是正確跳轉後的表現）

# --- 最佳實踐：輸入(Local) → 處理(UTC) → 輸出(Local) ---

# 假設使用者輸入一個不含時區資訊的字串
user_input = "2012-12-21 09:30:00"

# 1. 解析字串，得到一個「天真型 (Naive)」物件（無時區資訊）
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# 2. 賦予時區資訊 (replace)，並立即轉為 UTC (astimezone) 儲存至資料庫
# 注意：replace 是強制標籤，astimezone 是時間點對齊轉換
aware = naive.replace(tzinfo=central).astimezone(utc)

print(f"存入資料庫的 UTC 時間：{aware}")

# 3. 當另一位使用者（例如在台北）要查看時，再從 UTC 轉為其本地時區
display_taipei = aware.astimezone(ZoneInfo('Asia/Taipei'))
print(f"顯示在台北使用者的螢幕：{display_taipei}")
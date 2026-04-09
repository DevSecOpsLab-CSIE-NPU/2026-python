# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC
# 實務口訣：
# 輸入（含時區） -> 轉 UTC 儲存/計算 -> 輸出時再轉使用者時區
# 這個主題的核心不是 API 本身，而是建立正確的時間處理流程。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 建立常用時區物件。
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# ── 問題：直接在本地時間加減，夏令時邊界會出錯 ─────────
# 美國 2013-03-10 凌晨 2:00 會從時鐘上「直接跳到 3:00」，
# 也就是 2:xx 這一段本地時間其實不存在。
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 這裡若直接在本地時間上加 30 分鐘，
# 表面上會得到 2:15，但這個時刻在該時區那天根本不存在。
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間）

# ── 正確做法：先轉 UTC 計算，再轉回本地 ──────────────
# UTC 不受夏令時切換影響，所以拿來做內部計算最穩定。
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（自動跳過不存在的 2:xx）

# ── 最佳實踐：輸入 → UTC → 計算 → 輸出 ───────────────
# 模擬使用者輸入一個「沒有時區資訊」的本地時間字串。
user_input = "2012-12-21 09:30:00"

# strptime 解析後只會得到 naive datetime，
# 也就是「看起來像時間，但還不知道它屬於哪個時區」。
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# replace(tzinfo=central) 的語意是：
# 「把這個時間解釋成 Chicago 當地時間」。
# 之後再 astimezone(utc) 轉成 UTC，方便儲存與運算。
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")

# 輸出給不同地區使用者時，再從 UTC 轉到對方時區。
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

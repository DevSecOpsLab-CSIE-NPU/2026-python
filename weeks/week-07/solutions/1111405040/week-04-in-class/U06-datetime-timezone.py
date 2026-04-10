"""
U06. 時區操作最佳實踐：先轉 UTC 再計算。

重點：
1. 本地時間在夏令時切換點附近容易出現不存在或重複的時間。
2. 內部計算若直接用本地時間，較容易踩到邊界問題。
3. 常見做法是：輸入時轉 UTC、計算時用 UTC、輸出時再轉回目標時區。
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")


# ── 1. 直接在本地時間上做加減，可能碰到夏令時問題 ────────────
# 美國中部在 2013-03-10 凌晨 2 點切入夏令時。
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 這樣直接加 30 分鐘，理論上會得到 2:15，
# 但那一天的 2:xx 在當地其實不存在。
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")


# ── 2. 正確做法：先轉 UTC，再計算，再轉回本地 ──────────────
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")


# ── 3. 實務上常見流程：輸入 → UTC → 計算 → 顯示 ───────────
user_input = "2012-12-21 09:30:00"

# 先把字串解析成 naive datetime。
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# 假設使用者輸入的是 Chicago 當地時間，補上時區資訊後轉成 UTC。
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")

# 需要顯示給其他地區時，再轉換成對應時區。
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

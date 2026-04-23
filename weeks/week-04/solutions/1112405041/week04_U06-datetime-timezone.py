# 【Bloom 階段：U - 理解與進階應用】
# U06. 時區與日光節約時間 (DST) 的地雷
# August 的惡意提醒：這是很多資深工程師也會踩的坑。
# 在切換日光節約時間的當天，某些時間點根本不穩定。
# 解藥：邏輯運算一律用 UTC，只有顯示給用戶看時才轉為當地時間。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 芝加哥時區在 2013-03-10 凌晨 2:00 會跳過一小時 (DST 開始)
central = ZoneInfo("America/Chicago")
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# ❌ 錯誤的做法：直接加 local time (會噴錯或邏輯混亂)
# ✅ 正確做法：轉 UTC -> 加時間 -> 轉回 Local
utc_dt = local_dt.astimezone(ZoneInfo("UTC"))
result_utc = utc_dt + timedelta(minutes=30)
print(f"Correct Local Result: {result_utc.astimezone(central)}") # 3:15

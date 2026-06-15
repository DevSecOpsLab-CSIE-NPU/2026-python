# 【Bloom 階段：R - 記憶與基本操作】
# R09. 時區處理 (Timezones)
# August 的惡意提醒：永遠使用具備時區意識 (aware) 的 datetime。
# 否則在 Week 12 模擬網路交易時間差時，你會遇到離奇的 8 小時偏差。

from datetime import datetime
from zoneinfo import ZoneInfo

# 建立不同時區物件
utc = ZoneInfo("UTC")
taipei = ZoneInfo("Asia/Taipei")
central = ZoneInfo("America/Chicago")

# 1. 建立特定時區的時間
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(f"Chicago Time: {d}")

# 2. 轉換時區 (astimezone)
# 自動處理日光節約時間與時差
d_taipei = d.astimezone(taipei)
print(f"Taipei Time:  {d_taipei}")

# 3. 獲取當前時區時間
now_tw = datetime.now(tz=taipei)
print(f"Current TW:   {now_tw}")

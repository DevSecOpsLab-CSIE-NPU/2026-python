# U06. 時區操作最佳實踐：UTC 優先（3.16）
#
# 這個檔案要傳達的核心觀念是：
# 內部計算盡量使用 UTC，只有在顯示給使用者時才轉回本地時區。
# 原因是本地時間可能遇到夏令時間切換，會出現不存在或重複的時間點。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在本地時間做加減，遇到夏令時邊界時可能得到不存在的時刻。
# 美國 2013-03-10 凌晨 2:00 會跳到 3:00，也就是 2:xx 這段時間不存在。
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！）

# 正確做法：先把時間轉成 UTC，再做運算，最後需要顯示時再轉回本地。
# 這樣可以避開本地時區因為夏令時間而產生的跳躍問題。
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# 最佳實踐流程可以記成：輸入 → 轉 UTC → 做計算 → 顯示前再轉成本地時區。
# 這樣資料儲存與內部運算比較一致，也比較不容易踩到時區邊界問題。
user_input = "2012-12-21 09:30:00"
# 先解析成 naive datetime，尚未帶時區資訊。
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
# 把它視為中央時區時間，再轉為 UTC 存放。
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")
# 顯示給不同地區使用者時，再轉成對應時區，例如台北時間。
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

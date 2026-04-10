# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo # Python 3.9+ 建議使用的時區庫

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在具備時區資訊的本地時間加減，可能會遇到夏令時 (DST) 邊界錯誤
# 美國芝加哥 2013-03-10 從 2:00 跳到 3:00 (消失的 1 小時)
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 顯示 2:15，但實際上該時間點並不存在（時鐘已撥快）

# 正確做法：將所有時間先轉為 UTC 進行線性計算，最後才轉回本地顯示
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（正確反映了 1 小時的跳躍）

# 最佳實踐工作流：
# 1. 接收輸入 (naive datetime) -> 2. 給予時區 (aware) -> 3. 轉為 UTC 儲存/計算 -> 4. 輸出時轉本地時區
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")
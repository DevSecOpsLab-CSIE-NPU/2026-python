# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在本地時間加減，夏令時邊界會出錯
# 美國 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！）

# 正確做法：先轉 UTC 計算，再轉回本地
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

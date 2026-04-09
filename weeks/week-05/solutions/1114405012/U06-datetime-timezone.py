# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在本地時間加減，夏令時邊界會出錯
# 美國 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
# 本地時間在這種切換點附近可能會出現「不存在」或「重複」的時刻。
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
wrong = local_dt + timedelta(minutes=30)
print(f"直接在本地時間加 30 分鐘的結果：{wrong}")  # 2:15（不存在的時間）

# 正確做法：先轉 UTC 計算，再轉回本地
# UTC 不受夏令時影響，所以跨時區或跨 DST 計算時，先轉 UTC 會比較安全。
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"先轉 UTC 再計算的結果：{correct.astimezone(central)}")  # 3:15

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 真正實務上，建議內部都用 UTC 儲存與運算，只有顯示給使用者時才轉成當地時區。
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"轉成 UTC 儲存：{aware}")
print(f"顯示台北時間：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

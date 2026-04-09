# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 這份範例要說明一個實務上的核心原則：
# 內部儲存與運算最好一律使用 UTC，只有在輸入與輸出時才轉成當地時區。
# 原因是本地時間會遇到夏令時切換、重複時間與不存在時間等問題，直接計算很容易出錯。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# ZoneInfo 會載入 IANA 時區資料庫中的時區名稱。
# UTC 是標準時區；America/Chicago 代表美國芝加哥時區，會受夏令時影響。
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在本地時間加減，夏令時邊界會出錯
# 美國 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
# 這表示從 1:59 之後，時間會直接跳到 3:00，中間的 2:xx 並不存在。
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
# 如果直接對帶時區的本地時間做 timedelta 加法，看起來像是在做正常加法，
# 但實際上可能跨過不存在的時間區段，結果會變得不直覺。
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！）

# 正確做法：先轉 UTC 計算，再轉回本地
# 先把本地時間轉成 UTC，這樣時間軸是連續的，不會受夏令時跳躍影響。
utc_dt = local_dt.astimezone(utc)
# 在 UTC 上加減時間是安全的，因為 UTC 沒有夏令時切換。
correct = utc_dt + timedelta(minutes=30)
# 最後要顯示給使用者時，再轉回目標時區。
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 常見流程是：
# 1. 使用者輸入的是字串或本地時間。
# 2. 程式先把它解析成 datetime。
# 3. 在內部轉成 UTC 儲存或運算。
# 4. 真正要呈現給使用者時，再轉回當地時區。
user_input = "2012-12-21 09:30:00"
# 這裡先把字串解析成「naive datetime」：它沒有時區資訊，只表示一個表面時間。
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
# replace(tzinfo=...) 只是把時間標記成某時區，並不會自動調整數值本身。
# 因此這一步適合在你已確定輸入時間所屬時區時使用。
aware = naive.replace(tzinfo=central).astimezone(utc)
# 存到資料庫或內部系統時，建議統一使用 UTC，避免未來跨時區比對時出現混亂。
print(f"存 UTC：{aware}")
# 真正顯示給不同地區的使用者時，再轉換成對應時區即可。
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

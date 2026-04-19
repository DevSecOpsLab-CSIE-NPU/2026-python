# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

# 導入 datetime (日期時間) 和 timedelta (時間間隔) 類別
from datetime import datetime, timedelta
# 導入 ZoneInfo 類別，用於處理 IANA 時區資料庫 (Python 3.9+ 內建，官方建議用來取代舊的 pytz 模組)
from zoneinfo import ZoneInfo

# 建立 UTC 和美國中部時間 (芝加哥) 的時區物件
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago") 

# 問題：直接在本地時間加減，夏令時邊界會出錯
# 說明：美國中部時間在 2013-03-10 凌晨 2:00 開始實施夏令時間 (Daylight Saving Time)。
# 此時時鐘會直接往前撥一小時跳到 3:00，因此當天的 02:00:00 到 02:59:59 是「不存在」的時間。

# 建立一個時間點：2013年3月10日 凌晨 1:45，並明確指定為美國中部時區
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 錯誤示範：直接在帶有本地時區的 datetime 上加上 30 分鐘
wrong = local_dt + timedelta(minutes=30)
# 輸出結果會是 02:15，但在該時區當天的現實生活中，1:59 過後是直接變成 3:00 的！
print(f"錯誤結果：{wrong}")  # 2:15（這是一個在現實中不存在的時間！）

# 正確做法：先轉 UTC 計算，再轉回本地
# 說明：UTC 時區沒有夏令時的問題，時間是連續且線性的。
# 1. 先將本地時間轉換為 UTC 時間
utc_dt = local_dt.astimezone(utc)
# 2. 在 UTC 時間上進行加減運算
correct = utc_dt + timedelta(minutes=30)
# 3. 將計算後的正確 UTC 時間，再轉換回本地時區
# 輸出結果會正確地處理夏令時的跨越，顯示為 3:15
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 模擬使用者輸入的本地時間字串
user_input = "2012-12-21 09:30:00"
# 將字串解析為 naive datetime (不包含時區資訊的純數字日期時間)
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
# .replace(tzinfo=central) 賦予它原本的時區意義，接著 .astimezone(utc) 轉換為 UTC 時間
aware = naive.replace(tzinfo=central).astimezone(utc)
# 系統內部 (如資料庫儲存、日誌記錄、時間運算) 應該一律使用 UTC 時間
print(f"存 UTC：{aware}")  # 2012-12-21 15:30:00+00:00
# 當需要呈現給前端或使用者看時，再即時轉換為該使用者的目標時區
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")

# 10 模組、類別、例外與 Big-O（最低門檻）範例

# 從標準函式庫匯入雙向佇列 deque
from collections import deque

# 建立最多只能保留 2 個元素的 deque
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊

# 定義一個簡單的類別
class User:
    def __init__(self, user_id):
        # 把傳入的 user_id 存成物件屬性
        self.user_id = user_id

# 建立物件並讀取屬性
u = User(42)
uid = u.user_id

# 例外處理：檢查輸入是否可被轉成整數

def is_int(val):
    try:
        # 若可成功轉型，代表是整數字串或數值
        int(val)
        return True
    except ValueError:
        # 轉型失敗就捕捉 ValueError，回傳 False
        return False

# Big-O 只是觀念提示（描述輸入變大時的成本趨勢）
# list.append 通常是 O(1)
# list 切片是 O(N)

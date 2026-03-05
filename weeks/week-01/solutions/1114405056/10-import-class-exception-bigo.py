# 10 模組、類別、例外與 Big-O（最低門檻）範例

# 從 collections 模組匯入 deque 類別
# deque 是雙端隊列，可以高效地在兩端添加或移除元素
from collections import deque

# 創建一個最大長度為2的 deque
q = deque(maxlen=2)
q.append(1)  # 添加元素1
q.append(2)  # 添加元素2
q.append(3)  # 添加元素3，自動丟掉最舊的元素1，因為 maxlen=2
print("deque 內容:", list(q))  # 輸出：[2, 3]

# 定義一個 User 類別
class User:
    # __init__ 是建構函數，用來初始化物件
    def __init__(self, user_id):
        self.user_id = user_id  # 設定實例變數 user_id

# 創建 User 物件
u = User(42)
uid = u.user_id  # 取得 user_id
print("用戶 ID:", uid)  # 輸出：42

# 例外處理範例
# 定義一個函數來檢查值是否可以轉換為整數
def is_int(val):
    try:
        int(val)  # 嘗試將 val 轉換為整數
        return True  # 如果成功，返回 True
    except ValueError:  # 如果發生 ValueError 例外
        return False  # 返回 False

# 測試例外處理函數
print("123 是整數嗎?", is_int("123"))  # 輸出：True
print("abc 是整數嗎?", is_int("abc"))  # 輸出：False

# Big-O 只是觀念提示
# Big-O 表示演算法的時間或空間複雜度
# list.append 通常是 O(1) - 常數時間
# list 切片是 O(N) - 線性時間，N 是列表長度

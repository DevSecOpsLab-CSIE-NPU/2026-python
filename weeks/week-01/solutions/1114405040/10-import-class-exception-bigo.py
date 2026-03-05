# 10 模組、類別、例外與 Big-O（最低門檻）範例
# 本範例展示 Python 中導入模組、定義類別、處理例外，以及時間複雜度基本概念


# ========== 導入模組 (Importing Modules) ==========
# 從 collections 模組導入 deque（double-ended queue，雙端隊列）
# deque 是一個高效的隊列實現，支持在兩端快速添加和移除元素
from collections import deque


# ========== Deque 的使用 (Deque Usage) ==========
# 創建一個最大長度為 2 的 deque
# 當超過 maxlen 時，最舊的元素會自動被移除
q = deque(maxlen=2)

# 依序添加三個元素
q.append(1)  # q = deque([1], maxlen=2)
q.append(2)  # q = deque([1, 2], maxlen=2)
q.append(3)  # q = deque([2, 3], maxlen=2) — 元素 1 被自動丟掉


# ========== 類別定義與實例化 (Class Definition & Instantiation) ==========
# 定義一個 User 類別，用於表示使用者
class User:
    # 初始化方法：在創建新實例時調用
    # self 表示實例本身，user_id 是傳入的參數
    def __init__(self, user_id):
        # 將傳入的 user_id 儲存為實例屬性
        self.user_id = user_id

# 創建一個 User 實例，user_id 為 42
u = User(42)

# 訪問實例的屬性 user_id
uid = u.user_id  # uid = 42


# ========== 例外處理 (Exception Handling) ==========
# 定義一個函式，檢查給定的值是否能轉換為整數

def is_int(val):
    """
    檢查值 val 是否為整數或能轉換為整數
    
    參數:
        val: 待檢查的值
    
    返回:
        True: 如果 val 能成功轉換為整數
        False: 如果轉換過程中拋出 ValueError 例外
    """
    try:
        # 嘗試將 val 轉換為整數
        int(val)
        # 如果轉換成功，返回 True
        return True
    except ValueError:
        # 如果轉換失敗（例如 val="abc"），將捕獲 ValueError 例外
        # 然後返回 False
        return False


# ========== Big-O 時間複雜度 (Big-O Notation) ==========
# Big-O 表示法用於描述演算法的時間或空間複雜度
# O(n) 表示線性時間，O(1) 表示常數時間，O(n²) 表示平方時間，等等

# 常見操作的時間複雜度：
# - list.append(): O(1) — 平均情況下，向列表末尾添加元素是常數時間操作
# - list 切片 (e.g., list[1:3]): O(N) — 需要複製切片部分的所有元素
# - list.insert(0, x): O(N) — 需要移動現有元素為新元素騰出空間

# 10 模組、類別、例外與 Big-O（最低門檻）範例

# ========================================
# 1. 模組導入（import）
# ========================================
# 從 Python 內建的 collections 模組中導入 deque（雙端佇列）
from collections import deque

# deque 是一種特殊的序列，可以限制最大長度
# maxlen=2 表示最多只能存 2 個元素，超過會自動丟掉最舊的
q = deque(maxlen=2)
q.append(1)      # q 現在是 [1]
q.append(2)      # q 現在是 [1, 2]
q.append(3)      # 自動丟掉最舊的 1，q 現在是 [2, 3]

# ========================================
# 2. 類別定義（Class）
# ========================================
class User:
    # __init__ 是建構子，建立物件時會自動執行
    def __init__(self, user_id):
        # self 代表物件本身，self.user_id 是物件的屬性
        self.user_id = user_id

# 建立一個 User 物件，傳入 user_id = 42
u = User(42)
# 透過 . 運算子存取物件的屬性
uid = u.user_id

# ========================================
# 3. 例外處理（Exception Handling）
# ========================================

def is_int(val):
    """
    檢查一個值是否可以轉換成整數
    
    try-except 用來捕捉可能發生的錯誤：
    - try 區塊：執行可能出錯的程式碼
    - except 區塊：如果發生指定的錯誤，就執行這裡的程式碼
    """
    try:
        int(val)        # 嘗試將 val 轉成整數
        return True     # 成功就回傳 True
    except ValueError:  # 如果發生 ValueError（無法轉換）
        return False    # 就回傳 False

# ========================================
# 4. Big-O 觀念提示（時間複雜度）
# ========================================
# Big-O 用來描述演算法執行時間如何隨資料量增長
# 
# list.append(x) 通常是 O(1)：
#   不管串列有多長，加一個元素到尾端的時間固定
# 
# list[起:迄] 切片是 O(N)：
#   需要複製 N 個元素，所以時間正比於切片長度
#
# deque.append(x) 和 deque.appendleft(x) 都是 O(1)：
#   這是 deque 比 list 優秀的地方（兩端操作都很快）

# ========================================
# 輸出範例：看看每個部分的實際結果
# ========================================

print("=== 1. deque（有限長度的佇列） ===")
print(f"q 的內容: {q}")
print(f"類型: {type(q)}")
print("說明：因為 maxlen=2，append(3) 時自動丟掉最舊的 1")
print()

print("=== 2. 類別與物件 ===")
print(f"u 物件: {u}")
print(f"u.user_id: {u.user_id}")
print(f"uid 變數: {uid}")
print("說明：User(42) 建立一個物件，user_id 屬性存值 42")
print()

print("=== 3. 例外處理（測試 is_int 函式） ===")
print(f"is_int('123'): {is_int('123')}")      # True，可轉成整數
print(f"is_int('abc'): {is_int('abc')}")      # False，無法轉換
print(f"is_int('12.5'): {is_int('12.5')}")    # False，有小數點
print("說明：try-except 讓程式遇到錯誤不會崩潰，而是優雅處理")
print()

print("=== 4. Big-O 實際範例 ===")
# O(1) 操作：不論串列多長，時間都一樣
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # O(1)：直接加在尾端
print(f"append 後的 my_list: {my_list}")

# O(N) 操作：需要複製元素，時間正比於長度
sliced = my_list[1:4]  # O(N)：複製 3 個元素
print(f"切片 my_list[1:4]: {sliced}")
print("說明：切片要複製元素，所以比 append 慢")

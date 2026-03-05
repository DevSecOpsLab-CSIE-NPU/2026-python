# 10 模組、類別、例外與 Big-O（最低門檻）範例
# 這四個工具是解題的基礎工具包

# === PART 1: import 基礎 ===
# 為什麼要 import？
# 1. Python 內建工具包太豐富，各種資料結構都在模組中
# 2. deque, heapq, defaultdict 等是解題神器
# 3. 必須會用 import，否則無法使用高效的資料結構
from collections import deque

# deque（雙端隊列）的優勢
# 為什麼用 deque 而不是 list？
# 1. list.pop(0) 是 O(N)，deque.popleft() 是 O(1)
# 2. 適合「隊列」和「滑動窗口」問題
# 3. maxlen 屬性：自動丟掉最舊元素，適合滑動窗口
q = deque(maxlen=2)  # 建立最多容納 2 個元素的隊列
q.append(1)          # [1]
q.append(2)          # [1, 2]
q.append(3)          # [2, 3]（自動丟掉 1，保持 maxlen=2）

# === PART 2: class 與物件（看得懂即可） ===
# 為什麼需要 class？
# 1. 封裝資料和行為：一個物件可以有多個屬性
# 2. 簡化代碼：把相關資料綁在一起，不用用複雜 tuple
# 3. 題目中常見：PriorityQueue 中存放的物件、attrgetter 的用法
class User:
    def __init__(self, user_id):  # 初始化方法
        self.user_id = user_id    # 存儲屬性

u = User(42)      # 建立物件
uid = u.user_id   # 存取屬性：42

# === PART 3: 例外處理（try / except） ===
# 為什麼要 try/except？
# 1. 資料清潔：檢驗輸入是否合法
# 2. 避免程式崩潰：被零除、index out of range
# 3. 資料轉換：嘗試轉換，失敗就當作其他類型

def is_int(val):
    """判斷 val 是否能轉換成整數"""
    try:
        int(val)           # 嘗試轉換
        return True        # 成功就回傳 True
    except ValueError:     # 如果轉換失敗（如 "abc"）
        return False       # 回傳 False

# 使用例子
print(is_int("123"))   # True
print(is_int("abc"))   # False

# === PART 4: Big-O 觀念（聽得懂即可） ===
# 為什麼要懂 Big-O？
# 1. 選擇合適的資料結構：deque vs list 影響效能
# 2. 算法優化：sorted O(N log N) vs nlargest 的差別
# 3. LeetCode 題目的時間限制就是基於 Big-O

# 常見的 Big-O 時間複雜度：
# O(1) - 常數時間：dict.get()、list.append()、deque.popleft()
# O(N) - 線性時間：遍歷列表、list.pop(0)
# O(log N) - 對數時間：二分搜尋、heap push/pop
# O(N log N) - 最常見的排序時間：sorted()、heapq.nlargest()

# 為什麼選擇重要？
# - list.pop(0) 是 O(N) → deque.popleft() 改為 O(1)（1000 倍差異）
# - sorted() 是 O(N log N) → deque 用 O(N) 追蹤最小（效能差很多）

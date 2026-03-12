# 10 模組、類別、例外與 Big-O（最低門檻）範例

# ── import ───────────────────────────────────────────────
# import：從標準庫 collections 載入 deque（雙端佇列）
from collections import deque
from collections import defaultdict   # 另一個常用工具：預設值字典

# ── deque ────────────────────────────────────────────────
# deque(maxlen=2)：最多只保留 2 筆資料
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 超過容量時，自動丟掉最舊元素（1）
print(q)     # deque([2, 3], maxlen=2)

# appendleft / popleft：在「左端」操作，都是 O(1)
q2 = deque([10, 20, 30])
q2.appendleft(0)   # 從左邊插入 → deque([0, 10, 20, 30])
q2.popleft()       # 從左邊移除 → 0（常用來模擬 queue）
print(q2)          # deque([10, 20, 30])

# defaultdict：取不存在的 key 時自動建立預設值
counter = defaultdict(int)   # 預設值 0
for ch in 'aabbc':
    counter[ch] += 1         # 第一次碰到就從 0 開始加
print(dict(counter))         # {'a': 2, 'b': 2, 'c': 1}

# ── class ────────────────────────────────────────────────
# class：用來定義自訂型別（物件）
class User:
    # __init__ 是「建構子」，建立物件時自動呼叫
    def __init__(self, user_id, name):
        # self 代表「這個物件本身」，用來儲存屬性
        self.user_id = user_id
        self.name = name

    # 自訂 __repr__：print 物件時顯示什麼
    def __repr__(self):
        return f'User({self.user_id}, {self.name!r})'

    # 一般方法：操作物件自身的資料
    def greet(self):
        return f'Hi, I am {self.name}'


# 建立物件實例
u = User(42, 'Alice')
print(u)            # User(42, 'Alice')
print(u.greet())    # Hi, I am Alice
uid = u.user_id     # 存取屬性

# ── 例外處理 ──────────────────────────────────────────────
# 例外處理：嘗試把輸入轉成整數
# 成功回傳 True，失敗（ValueError）回傳 False
# 適合做輸入驗證

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


print(is_int('123'))   # True
print(is_int('abc'))   # False

# 可以同時捕捉多種例外
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None          # 除以零回傳 None
    except TypeError:
        return None          # 型別不對也回傳 None
    finally:
        pass                 # finally 不論成功失敗都會執行（常用來關閉檔案）


print(safe_div(10, 2))    # 5.0
print(safe_div(10, 0))    # None

# ── Big-O 觀念提示 ────────────────────────────────────────
# Big-O 只描述「資料量 N 變大時，執行時間的成長速度」
# O(1)   常數時間：list.append、dict 查詢（大多數情況）
# O(log N)       ：二分搜尋
# O(N)   線性時間：for 迴圈走一遍、list 切片（複製 N 個元素）
# O(N²)  平方時間：兩層 for 迴圈（氣泡排序）

# 範例：O(N) vs O(N²) 的差異
data = list(range(100))

# O(N)：只走一遍
total = sum(data)            # 100 次加法

# O(N²)：兩層迴圈
pairs_count = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        pairs_count += 1     # 約 100*99/2 = 4950 次
print(pairs_count)           # 4950

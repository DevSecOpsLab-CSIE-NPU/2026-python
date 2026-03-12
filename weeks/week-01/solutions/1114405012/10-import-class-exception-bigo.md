# 10 模組、類別、例外與 Big-O（最低門檻）

## 📦 import 基礎

你必須已經「不需要解釋」就能看懂：

```python
# import：匯入整個模組
import heapq
# 使用時需要加上模組名稱：heapq.heappush(...)

# from ... import：只匯入特定功能
from collections import deque
# 使用時直接呼叫：deque([1, 2, 3])

# 其他常見寫法：
from collections import defaultdict, Counter  # 匯入多個
import numpy as np  # 使用別名
from math import *  # 匯入所有（不建議，容易命名衝突）
```

**常用模組速查**：
```python
# 資料結構
from collections import deque, Counter, defaultdict, OrderedDict
from heapq import heappush, heappop, nlargest, nsmallest
from queue import Queue, PriorityQueue

# 工具函式
from itertools import groupby, accumulate, combinations
from operator import itemgetter, attrgetter
from functools import lru_cache  # 快取裝飾器

# 其他
import bisect  # 二分搜尋
import re      # 正規表達式
import math    # 數學函式
```

用途（對應第一章範例）：
- 幾乎所有進階工具都需要 import

---

## 🎨 class 與物件（看得懂即可）

```python
# 定義一個類別（class）
class User:
    # __init__ 是建構子（constructor），建立物件時會自動執行
    def __init__(self, user_id):
        # self 代表「這個物件本身」
        # self.user_id 是「物件的屬性」
        self.user_id = user_id
    
# 建立物件的方式：
user = User(123)  # 呼叫 __init__，傳入 user_id=123
```

```python
# 存取物件的屬性
user.user_id  # 取得值：123
```

**完整範例**：
```python
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id  # 屬性 1
        self.name = name        # 屬性 2
    
    # 定義方法（method）
    def greet(self):
        return f"Hello, I'm {self.name}"

# 使用
user = User(123, "Alice")
print(user.user_id)   # 123
print(user.name)      # Alice
print(user.greet())   # Hello, I'm Alice
```

**為什麼需要 class？**
```python
# 情境：管理優先佇列中的任務

# ❌ 使用 tuple（不清楚每個位置代表什麼）
task = (1, 100, "send_email")  # (優先級, 時間戳, 任務名稱) ← 容易混淆

# ✅ 使用 class（一目了然）
class Task:
    def __init__(self, priority, timestamp, name):
        self.priority = priority
        self.timestamp = timestamp
        self.name = name

task = Task(1, 100, "send_email")
print(task.priority)  # 清楚知道這是優先級
```

用途（對應第一章範例）：
- **PriorityQueue Item**：封裝優先佇列的項目
- **attrgetter**：取得物件屬性（`attrgetter('user_id')` 取 `user.user_id`）
- **namedtuple 對照 class**：簡化版的 class

**namedtuple vs class**：
```python
from collections import namedtuple

# namedtuple：輕量級，不可修改（immutable）
User = namedtuple('User', ['user_id', 'name'])
user = User(123, "Alice")
# user.user_id = 456  # ❌ 錯誤！不能修改

# class：完整功能，可修改
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

user = User(123, "Alice")
user.user_id = 456  # ✅ 可以修改
```

---

## 🛡️ 例外處理（try / except）

```python
# try-except：處理可能發生的錯誤
try:
    # 嘗試執行的程式碼
    int(val)  # 如果 val 不是數字格式會出錯
except ValueError:
    # 發生 ValueError 時執行
    pass  # pass 表示什麼都不做
```

**完整範例**：
```python
def is_int(s):
    """檢查字串是否可以轉換成整數"""
    try:
        int(s)
        return True
    except ValueError:
        return False

# 測試
print(is_int("123"))    # True
print(is_int("12.5"))   # False
print(is_int("abc"))    # False
```

**常見例外類型**：
```python
# ValueError：值的格式錯誤
int("abc")  # ValueError: invalid literal for int()

# KeyError：字典找不到鍵
d = {'a': 1}
d['b']  # KeyError: 'b'

# IndexError：索引超出範圍
lst = [1, 2, 3]
lst[10]  # IndexError: list index out of range

# ZeroDivisionError：除以零
10 / 0  # ZeroDivisionError: division by zero
```

**進階用法**：
```python
# 捕捉多種例外
try:
    result = int(val) / divisor
except ValueError:
    print("無法轉換成整數")
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:  # 捕捉所有例外
    print(f"發生錯誤：{e}")
else:
    print("成功執行")  # 沒有例外時執行
finally:
    print("無論如何都會執行")  # 清理資源用
```

用途（對應第一章範例）：
- **`filter(is_int, values)`**：過濾出可轉換成整數的值

```python
# 實際應用範例
data = ["123", "45.6", "abc", "789", "xyz"]

# 過濾出可以轉換成整數的字串
valid_numbers = list(filter(is_int, data))
print(valid_numbers)  # ['123', '789']

# 轉換成整數
numbers = [int(x) for x in valid_numbers]
print(numbers)  # [123, 789]
```

---

## ⚡ 基本 Big-O 觀念（聽得懂即可）

你需要知道：

### O(1) - 常數時間
```python
# 無論資料多大，執行時間固定
lst = [1, 2, 3, 4, 5]
x = lst[0]        # O(1) - 直接取值
d = {'a': 1}
y = d['a']        # O(1) - 字典查詢
```

### O(N) - 線性時間
```python
# 資料量增加，執行時間等比增加
lst = [1, 2, 3, 4, 5]
for x in lst:     # O(N) - 遍歷所有元素
    print(x)

if 3 in lst:      # O(N) - 搜尋列表（最差需要看完所有元素）
    pass
```

### O(log N) - 對數時間
```python
# 每次操作都把問題規模減半（超快！）
import bisect
sorted_lst = [1, 3, 5, 7, 9]
index = bisect.bisect_left(sorted_lst, 5)  # O(log N) - 二分搜尋
```

### 時間複雜度比較
```python
# 假設 N = 1,000,000
# O(1)      →        1 次操作 ⚡⚡⚡
# O(log N)  →       20 次操作 ⚡⚡
# O(N)      →  1,000,000 次操作 ⚡
# O(N²)     → 1,000,000,000,000 次操作 🐌
```

用途（對應第一章範例）：

### 1️⃣ deque vs list（為什麼要用 deque？）

```python
from collections import deque

# list 的問題：
lst = [1, 2, 3]
lst.append(4)      # O(1) - 尾端加入 ✅
lst.pop()          # O(1) - 尾端刪除 ✅
lst.insert(0, 0)   # O(N) - 開頭插入 ❌ 慢！需要移動所有元素
lst.pop(0)         # O(N) - 開頭刪除 ❌ 慢！需要移動所有元素

# deque 的優勢：
dq = deque([1, 2, 3])
dq.append(4)       # O(1) - 尾端加入 ✅
dq.pop()           # O(1) - 尾端刪除 ✅
dq.appendleft(0)   # O(1) - 開頭加入 ✅ 快！
dq.popleft()       # O(1) - 開頭刪除 ✅ 快！

# 結論：需要頻繁操作開頭時使用 deque
```

### 2️⃣ heap push/pop（優先佇列的效率）

```python
import heapq

heap = []
# heappush：O(log N) - 插入元素並維持堆積特性
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# heappop：O(log N) - 取出最小值
min_val = heapq.heappop(heap)  # 1

# 為什麼不用 sorted？
# sorted(lst)[0] → O(N log N)，太慢！
# heappop(heap)  → O(log N)，快很多！
```

### 3️⃣ sorted vs nlargest（找前 N 名的最佳解）

```python
from heapq import nlargest

data = list(range(1000000))  # 一百萬筆資料

# 方法 1：sorted - O(N log N)
top10 = sorted(data, reverse=True)[:10]  # 慢！需要排序全部

# 方法 2：nlargest - O(N log K)，K=10
top10 = nlargest(10, data)  # 快！只維護大小為 10 的 heap

# 結論：
# - 需要全部排序 → 用 sorted
# - 只需要前 K 名且 K << N → 用 nlargest/nsmallest
```

## 📊 時間複雜度速查表

| 操作 | list | deque | set/dict | heap |
|------|------|-------|----------|------|
| 取值 `[i]` | O(1) | O(N) | - | - |
| 搜尋 `in` | O(N) | O(N) | O(1) | - |
| 尾端加入 | O(1) | O(1) | O(1) | O(log N) |
| 開頭加入 | O(N) | O(1) | - | - |
| 尾端刪除 | O(1) | O(1) | O(1) | - |
| 開頭刪除 | O(N) | O(1) | - | O(log N) |
| 排序 | O(N log N) | O(N log N) | - | - |

## 💡 學習重點

1. **import**：熟記常用模組，知道何時需要匯入什麼工具
2. **class**：看得懂別人的程式碼即可，初期不用深入
3. **try-except**：處理可預期的錯誤，避免程式崩潰
4. **Big-O**：
   - 選對資料結構：需要頻繁操作開頭用 `deque`，需要快速查找用 `set/dict`
   - 選對演算法：找 Top-K 用 `nlargest`，不要用 `sorted`
   - 避免巢狀迴圈：小心 O(N²) 的效能陷阱

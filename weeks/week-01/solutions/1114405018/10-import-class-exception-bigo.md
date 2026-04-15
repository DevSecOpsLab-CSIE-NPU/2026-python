# 10 模組、類別、例外與 Big-O（最低門檻）

## 概述

這一章是 Python 進階實作的「門檻知識」。你要能看懂模組匯入、類別基本結構、例外處理，以及常見操作的時間複雜度。

你必須已經「不需要解釋」就能看懂：

```python
import heapq
from collections import deque

class User:
    def __init__(self, user_id):
        self.user_id = user_id

try:
    int(val)
except ValueError:
    pass
```

---

## import 基礎

### 為什麼需要 import

Python 的標準函式庫很大，你通常不會把所有功能寫在同一個檔案。`import` 讓你載入外部模組與工具，提升重用性與可維護性。

```python
# 載入整個模組
import math
print(math.sqrt(16))  # 4.0

# 只載入模組中的特定名稱
from math import sqrt
print(sqrt(25))       # 5.0

# 取別名
import numpy as np
arr = np.array([1, 2, 3])
```

### 常見 import 方式

```python
# 方式 1：import module
import heapq
nums = [5, 1, 4]
heapq.heapify(nums)

# 方式 2：from module import name
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)

# 方式 3：from module import name as alias
from collections import defaultdict as dd
counter = dd(int)
counter['a'] += 1
```

### `import x` 與 `from x import y` 差異

```python
import math
print(math.pi)      # 需要模組前綴

from math import pi
print(pi)           # 直接使用名稱
```

1. `import x` 優點：命名空間清楚，不容易撞名。
2. `from x import y` 優點：寫法簡潔。
3. 大型專案通常偏好 `import x` 或明確的 `from x import y`，避免 `import *`。

### 不建議使用 `import *`

```python
# ❌ 不建議
from math import *

# 問題：你不知道有哪些名稱進來，且容易覆蓋原本變數
```

### 常見標準庫（第一章常見到）

```python
import heapq                 # 堆積，做 Top-N、優先隊列
from collections import deque # 雙端佇列
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, attrgetter
```

用途（對應第一章範例）：

- 幾乎所有進階工具
- Top-N、分組、排序 key、高效 queue

---

## class 與物件（看得懂即可）

### 類別與物件基本概念

`class` 是藍圖，`object`（物件）是依藍圖建立出的實例。

```python
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

user1 = User(101, 'Alice')
user2 = User(102, 'Bob')

print(user1.user_id)  # 101
print(user2.name)     # Bob
```

### `__init__` 與 `self`

```python
class Product:
    def __init__(self, name, price):
        # self 代表「這個物件本身」
        self.name = name
        self.price = price

apple = Product('apple', 1.5)
print(apple.name)   # apple
print(apple.price)  # 1.5
```

1. `__init__` 是初始化方法，在建立物件時自動呼叫。
2. `self.xxx` 是「物件屬性」，每個實例都可有不同值。

### 屬性存取

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id

user = User(2001)
print(user.user_id)  # 2001

user.user_id = 3001
print(user.user_id)  # 3001
```

### `__repr__` 讓除錯更好讀

```python
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}')"

u = User(1, 'Alice')
print(u)  # User(user_id=1, name='Alice')
```

### class 在排序中的用途

```python
from operator import attrgetter

class Item:
    def __init__(self, priority, index, value):
        self.priority = priority
        self.index = index
        self.value = value

items = [
    Item(2, 0, 'urgent'),
    Item(1, 1, 'normal'),
    Item(1, 2, 'later'),
]

# 先比 priority，再比 index
sorted_items = sorted(items, key=attrgetter('priority', 'index'))
```

用途（對應第一章範例）：

- PriorityQueue item 封裝
- `attrgetter` 排序
- `namedtuple` 與 class 對照

---

## 例外處理（try / except）

### 為什麼要做例外處理

程式會遇到不可預期輸入，例如字串轉數字失敗、檔案不存在、索引越界。例外處理讓程式「可控地失敗」。

```python
try:
    n = int('123')
    print(n)
except ValueError:
    print('轉換失敗')
```

### 基本語法

```python
try:
    # 可能出錯的程式碼
    risky_code()
except SpecificError:
    # 對應錯誤的處理
    handle_error()
else:
    # 沒有例外才執行
    on_success()
finally:
    # 不論是否出錯都會執行
    cleanup()
```

### 常見例外類型

```python
# ValueError：值型態不正確
try:
    int('abc')
except ValueError:
    print('不是合法整數')

# ZeroDivisionError：除以 0
try:
    x = 10 / 0
except ZeroDivisionError:
    print('除數不能是 0')

# KeyError：字典鍵不存在
d = {'a': 1}
try:
    print(d['b'])
except KeyError:
    print('key 不存在')

# IndexError：索引越界
arr = [10, 20]
try:
    print(arr[5])
except IndexError:
    print('索引超出範圍')
```

### 在資料清洗中的典型用法

```python
values = ['12', '7', 'abc', '3.5', '-2']

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

int_values = list(filter(is_int, values))
print(int_values)  # ['12', '7', '-2']
```

### 不要濫用 `except:`

```python
# ❌ 不建議：捕捉所有錯誤，可能吞掉真正 bug
try:
    do_something()
except:
    pass

# ✅ 建議：捕捉明確錯誤
try:
    do_something()
except ValueError as e:
    print(f'資料格式錯誤: {e}')
```

用途（對應第一章範例）：

- `filter(is_int, values)`
- 資料解析與容錯

---

## 基本 Big-O 觀念（聽得懂即可）

### Big-O 是什麼

Big-O 描述「輸入規模 $N$ 增加時，執行時間如何成長」。

你至少要知道：

- $O(1)$：常數時間
- $O(N)$：線性時間
- $O(\log N)$：對數時間
- $O(N\log N)$：排序常見複雜度

### 常見操作複雜度速查

```text
list append           -> O(1) 平均
list insert(0, x)     -> O(N)
list pop()            -> O(1)
list pop(0)           -> O(N)

deque append/appendleft -> O(1)
deque pop/popleft       -> O(1)

dict 查找 key         -> O(1) 平均
set 成員測試 in       -> O(1) 平均

heapq heappush/heappop -> O(log N)
sorted()               -> O(N log N)
heapq.nlargest(k, xs)  -> O(N log k)
```

### `deque` vs `list`

```python
from collections import deque

# list 左側操作慢（O(N)）
arr = [1, 2, 3]
arr.insert(0, 0)   # 需要搬移元素

# deque 左右兩側操作都快（O(1)）
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.popleft()
```

### `sorted` vs `nlargest`

```python
import heapq

nums = [9, 1, 7, 3, 10, 5, 6, 8, 2, 4]

# 只要前 3 大
top3_a = sorted(nums, reverse=True)[:3]   # O(N log N)
top3_b = heapq.nlargest(3, nums)          # O(N log 3)

print(top3_a)  # [10, 9, 8]
print(top3_b)  # [10, 9, 8]
```

當 $k \ll N$（例如只取前 10 名，但總資料 100 萬筆），`nlargest` 通常更省時間。

### 直覺記憶法

1. `O(1)` 幾乎不怕資料變大。
2. `O(N)` 資料翻倍，時間大致翻倍。
3. `O(log N)` 資料翻倍，時間只增加一點點。
4. `O(N log N)` 常見於排序。

用途（對應第一章範例）：

- `deque` vs `list`
- heap push/pop
- `sorted` vs `nlargest`

---

## 綜合實例

```python
from collections import deque
import heapq

class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __repr__(self):
        return f"Task(priority={self.priority}, name='{self.name}')"

raw_tasks = [
    ('2', 'write report'),
    ('x', 'invalid priority'),
    ('1', 'fix bug'),
    ('3', 'review PR'),
]

queue = deque()
heap = []

for p_str, name in raw_tasks:
    try:
        p = int(p_str)
        task = Task(p, name)
        queue.append(task)               # O(1)
        heapq.heappush(heap, (p, name))  # O(log N)
    except ValueError:
        # 遇到非法優先級，略過
        continue

print('Queue:', list(queue))
print('Top priority:', heapq.nsmallest(1, heap))
```

這段程式同時展示了：

- `import`：載入標準庫
- `class`：封裝任務資料
- `try/except`：容錯解析
- Big-O 直覺：`deque.append` 是 $O(1)$，`heappush` 是 $O(\log N)$

---

## 重要提示

1. `import` 建議明確，不要濫用 `import *`。
2. 類別最少要看懂 `__init__`、`self`、屬性存取。
3. 例外處理請捕捉具體錯誤類型，不要把所有錯誤都 `pass`。
4. 想做效能選型時，先判斷你是要「全部排序」還是「只要 Top-N」。
5. `groupby`、`heapq`、`deque` 都是第一章常見的高價值工具。

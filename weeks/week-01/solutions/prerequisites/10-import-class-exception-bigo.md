# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq
from collections import deque
```

用途（對應第一章範例）：

- 幾乎所有進階工具

---

## class 與物件（看得懂即可）

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
```

```python
user.user_id
```

用途（對應第一章範例）：

- PriorityQueue Item
- attrgetter
- namedtuple 對照 class

---

## 例外處理（try / except）

```python
try:
    int(val)
except ValueError:
    pass
```

用途（對應第一章範例）：

- `filter(is_int, values)`

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)

用途（對應第一章範例）：

- deque vs list
- heap push/pop
- sorted vs nlargest

## 註釋版範例（可直接貼到程式）

```python
import heapq
from collections import deque


# 1) import：拿工具來用
nums = [7, 2, 9, 1]
heapq.heapify(nums)  # 就地轉成最小堆
heapq.heappush(nums, 3)  # O(log N)
smallest = heapq.heappop(nums)  # O(log N)
print("smallest:", smallest)


# 2) class 與物件：把資料封裝在物件中
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


u = User(10, "amy")
print(u.user_id, u.name)  # 10 amy


# 3) try/except：處理可能失敗的轉型
values = ["12", "x", "7", "-3", "hello"]
ints = []
for val in values:
    try:
        ints.append(int(val))
    except ValueError:
        # 不是整數字串就跳過，程式不中斷
        pass
print(ints)  # [12, 7, -3]


# 4) Big-O 直覺示例
dq = deque([1, 2, 3])
dq.appendleft(0)  # 頭部插入通常 O(1)

lst = [1, 2, 3]
lst.insert(0, 0)  # 頭部插入通常 O(N)，因為需要搬移元素

# 只取 Top-2：可用 nlargest，常比全排序切片更省
scores = [35, 99, 76, 88, 60]
top2 = heapq.nlargest(2, scores)
print("top2:", top2)  # [99, 88]
```
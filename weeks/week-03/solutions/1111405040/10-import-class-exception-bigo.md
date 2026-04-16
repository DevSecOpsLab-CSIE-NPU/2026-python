# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq
from collections import deque
```

用途（對應第一章範例）：

- 幾乎所有進階工具

### import 的讀法

```python
import heapq
```

這代表載入整個 `heapq` 模組，使用時要寫模組名稱：

```python
heapq.heappush(heap, item)
```

```python
from collections import deque
```

這代表只從 `collections` 裡匯入 `deque`，使用時可以直接寫：

```python
queue = deque()
```

兩種寫法都可以，差別在於使用時是否需要加上模組名稱。

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

### class 的基本觀念

`class` 用來描述一種資料型態。

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
```

這段程式表示每個 `User` 物件都有一個 `user_id` 屬性。

建立物件：

```python
user = User(1001)
```

讀取屬性：

```python
print(user.user_id)
```

在第一章範例中，class 常用來建立帶有屬性的資料，例如使用 `attrgetter()` 排序物件。

---

## namedtuple 與 class 的對照

`namedtuple` 可以用比較短的方式建立簡單資料結構。

```python
from collections import namedtuple

User = namedtuple("User", ["user_id"])
user = User(1001)
```

這時一樣可以讀取：

```python
user.user_id
```

簡單資料可以用 `namedtuple`；如果需要方法、驗證或較多行為，通常會改用 class。

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

### try / except 的用途

例外處理用來處理「可能失敗，但不一定代表程式要中止」的情況。

```python
try:
    int(val)
except ValueError:
    pass
```

這段意思是：

- 嘗試把 `val` 轉成整數
- 如果轉換失敗，會發生 `ValueError`
- 發生錯誤時不讓程式中止，而是進入 `except` 區塊

常見應用是判斷字串能不能轉成整數：

```python
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
```

這樣就可以搭配 `filter()` 留下能轉成整數的資料。

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)

用途（對應第一章範例）：

- deque vs list
- heap push/pop
- sorted vs nlargest

### O(1)

O(1) 表示操作時間大致固定，不會因為資料變多而明顯增加。

例子：

```python
data[0]
```

從 list 取指定索引通常是 O(1)。

### O(N)

O(N) 表示操作時間會跟資料量成正比。

例子：

```python
for item in data:
    print(item)
```

如果有 N 筆資料，就會跑 N 次。

### O(log N)

O(log N) 表示資料變多時，操作時間增加得比較慢。

常見例子是 heap 的 push / pop：

```python
heapq.heappush(heap, item)
heapq.heappop(heap)
```

heap 不需要每次都把全部資料重新排序，因此在只需要維護最小值或最大值時很常用。

### deque vs list

`deque` 適合從兩端加入或移除資料。

```python
queue.appendleft(item)
queue.popleft()
```

如果用 list 做 `pop(0)`，前面的元素被移除後，後面的元素需要往前搬，成本通常較高。

### sorted vs nlargest

`sorted()` 會排序全部資料。

`heapq.nlargest(n, data)` 只找前 n 大。

如果只需要少數幾筆最大值，`nlargest()` 通常更符合需求。

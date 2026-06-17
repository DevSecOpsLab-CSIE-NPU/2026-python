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

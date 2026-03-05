# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq  # 匯入 heapq 模組，用於實現堆積（heap）資料結構，提供優先佇列等功能
from collections import deque  # 從 collections 模組匯入 deque 類別，用於雙端佇列（double-ended queue），支援高效的兩端操作
```

用途（對應第一章範例）：

- 幾乎所有進階工具

---

## class 與物件（看得懂即可）

```python
class User:  # 定義一個名為 User 的類別，用於表示使用者
    def __init__(self, user_id):  # 初始化方法（建構子），在建立物件時自動呼叫，接收 user_id 參數
        self.user_id = user_id  # 將參數 user_id 賦值給物件的實例變數 self.user_id
```

```python
user.user_id  # 存取物件 user 的 user_id 屬性
```

用途（對應第一章範例）：

- PriorityQueue Item
- attrgetter
- namedtuple 對照 class

---

## 例外處理（try / except）

```python
try:  # 嘗試執行以下程式碼區塊
    int(val)  # 將變數 val 轉換為整數，如果 val 不是有效的整數字串會引發 ValueError
except ValueError:  # 如果在 try 區塊中發生 ValueError 例外，則執行此區塊
    pass  # 什麼都不做，忽略這個錯誤
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

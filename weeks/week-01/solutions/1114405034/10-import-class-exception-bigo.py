# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
# 匯入整個模組：使用時需要模組名稱作為前綴
import heapq

# 從模組中匯入特定函數或類別：可以直接使用
from collections import deque
```

用途（對應第一章範例）：

- 幾乎所有進階工具：Python 的標準庫和第三方庫都需要 import

---

## class 與物件（看得懂即可）

```python
# 定義類別：User 類別用來表示用戶
class User:
    # __init__ 是建構函數，物件建立時自動呼叫
    def __init__(self, user_id):
        # self 表示物件本身，user_id 是實例變數
        self.user_id = user_id
```

```python
# 存取物件屬性：使用點號運算子
user.user_id
```

用途（對應第一章範例）：

- PriorityQueue Item：自定義類別作為優先隊列的元素
- attrgetter：用於從物件中提取屬性值
- namedtuple 對照 class：namedtuple 是輕量級的類別替代方案

---

## 例外處理（try / except）

```python
# try 區塊：嘗試執行可能會出錯的程式碼
try:
    int(val)  # 嘗試將 val 轉換為整數
# except 區塊：當發生指定例外時執行
except ValueError:  # 如果 val 不是有效數字，會拋出 ValueError
    pass  # 忽略錯誤，繼續執行
```

用途（對應第一章範例）：

- `filter(is_int, values)`：在過濾函數中使用例外處理來檢查值是否為整數

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1)：常數時間，無論數據大小，操作時間固定
- O(N)：線性時間，操作時間與數據大小成正比
- O(log N)：對數時間，操作時間隨數據大小增加而緩慢增加

用途（對應第一章範例）：

- deque vs list：deque 的兩端操作是 O(1)，list 的中間插入是 O(N)
- heap push/pop：堆積的插入和刪除是 O(log N)
- sorted vs nlargest：sorted 是 O(N log N)，nlargest 是 O(N log K) 更高效

# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq  # 匯入 heapq 模組，用於堆操作
from collections import deque  # 從 collections 模組匯入 deque 類別，用於雙端隊列
```

用途（對應第一章範例）：

- 幾乎所有進階工具  # 這些模組提供高效的資料結構和演算法

---

## class 與物件（看得懂即可）

```python
class User:  # 定義一個 User 類別
    def __init__(self, user_id):  # 初始化方法，設定實例變數
        self.user_id = user_id  # 將 user_id 儲存為實例屬性
```

```python
user.user_id  # 存取物件的屬性
```

用途（對應第一章範例）：

- PriorityQueue Item  # 用類別定義優先隊列中的項目
- attrgetter  # 使用類別屬性進行排序或存取
- namedtuple 對照 class  # namedtuple 類似於簡單的類別

---

## 例外處理（try / except）

```python
try:
    int(val)  # 嘗試將 val 轉換為整數
except ValueError:  # 如果發生 ValueError 例外
    pass  # 忽略錯誤
```

用途（對應第一章範例）：

- `filter(is_int, values)`  # 在過濾函式中使用例外處理來檢查是否為整數

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)  # 常數時間、線性時間、對數時間複雜度

用途（對應第一章範例）：

- deque vs list  # deque 在兩端操作是 O(1)，list 是 O(N)
- heap push/pop  # 堆的插入和刪除是 O(log N)
- sorted vs nlargest  # sorted 是 O(N log N)，nlargest 使用堆是 O(N log K)

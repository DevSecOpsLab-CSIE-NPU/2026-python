# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq  # 導入 heapq 模組，提供堆隊列演算法，用於實現優先隊列
from collections import deque  # 從 collections 模組中導入 deque 類別，一種雙端隊列資料結構
```

用途（對應第一章範例）：

- 幾乎所有進階工具：這些模組提供了高效的資料結構和演算法，是實現複雜功能的基本工具

---

## class 與物件（看得懂即可）

```python
class User:  # 定義一個名為 User 的類別
    def __init__(self, user_id):  # __init__ 方法是建構函式，用於初始化物件的屬性
        self.user_id = user_id  # 將參數 user_id 賦值給物件的 user_id 屬性
```

```python
user.user_id  # 訪問物件 user 的 user_id 屬性
```

用途（對應第一章範例）：

- PriorityQueue Item：使用類別來定義優先隊列中的項目，以便存儲更多資訊
- attrgetter：使用類別屬性來定義排序或提取的依據
- namedtuple 對照 class：namedtuple 類似於簡單的類別，用於創建輕量級的物件

---

## 例外處理（try / except）

```python
try:  # 嘗試執行以下代碼塊
    int(val)  # 嘗試將 val 轉換為整數
except ValueError:  # 如果發生 ValueError 例外，執行以下代碼
    pass  # 不做任何處理，繼續執行
```

用途（對應第一章範例）：

- `filter(is_int, values)`：在過濾函式中使用例外處理來檢查值是否可以轉換為整數

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)

用途（對應第一章範例）：

- deque vs list
- heap push/pop
- sorted vs nlargest

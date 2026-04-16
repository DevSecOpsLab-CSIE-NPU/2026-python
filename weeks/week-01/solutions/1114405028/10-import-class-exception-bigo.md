# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎

你必須已經「不需要解釋」就能看懂：

```python
import heapq  # 匯入 heapq 模組：提供堆資料結構的實現，用於優先隊列等應用。
from collections import deque  # 從 collections 模組匯入 deque：雙端隊列，支援高效的兩端插入和刪除操作。
```

用途（對應第一章範例）：

- 幾乎所有進階工具  # 這些標準庫模組提供高效的資料結構和演算法，是 Python 高效程式設計的基礎。

---

## class 與物件（看得懂即可）

```python
class User:  # 定義 User 類別：類別是物件的藍圖，封裝資料和行為。
    def __init__(self, user_id):  # __init__ 方法：建構函式，在創建物件時自動呼叫，用來初始化實例變數。
        self.user_id = user_id  # self.user_id：實例屬性，儲存每個 User 物件的 user_id。
```

```python
user.user_id  # 存取物件屬性：通過點運算子存取物件的屬性值。
```

用途（對應第一章範例）：

- PriorityQueue Item  # 使用類別定義優先隊列中的項目，可以封裝更多資訊。
- attrgetter  # 使用類別屬性進行排序或存取，例如 operator.attrgetter('price')。
- namedtuple 對照 class  # namedtuple 類似於輕量級類別，提供不可變的物件，但更簡單。

---

## 例外處理（try / except）

```python
try:
    int(val)  # 嘗試執行：將 val 轉換為整數，如果 val 不是有效數字，會引發 ValueError。
except ValueError:  # 捕獲例外：如果發生 ValueError，執行 except 區塊的程式碼。
    pass  # 忽略錯誤：這裡選擇忽略錯誤，可以根據需要處理或記錄。
```

用途（對應第一章範例）：

- `filter(is_int, values)`  # 在過濾函式中使用例外處理來檢查值是否為整數，例如定義 is_int 函式來測試轉換。

---

## 基本 Big-O 觀念（聽得懂即可）

你需要知道：

- O(1), O(N), O(log N)  # Big-O 表示法描述演算法的時間或空間複雜度。O(1) 為常數時間，O(N) 為線性時間，O(log N) 為對數時間。

用途（對應第一章範例）：

- deque vs list  # deque 的 append/pop 操作是 O(1)，而 list 的 insert/pop(0) 是 O(N)，因為需要移動元素。
- heap push/pop  # 堆的插入和刪除操作是 O(log N)，因為需要維護堆的結構。
- sorted vs nlargest  # sorted 對整個列表排序是 O(N log N)，而 heapq.nlargest 使用堆是 O(N log K)，當 K 較小時更高效。

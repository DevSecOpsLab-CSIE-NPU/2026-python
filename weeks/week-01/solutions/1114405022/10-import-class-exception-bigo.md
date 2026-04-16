
# 10 模組、類別、例外與 Big-O（最低門檻）

## import 基礎
```python
import heapq              # 匯入 heapq 模組，提供 heap 資料結構
from collections import deque  # 匯入 deque，提供雙向佇列
```
用途：引入標準函式庫的進階工具，讓程式更強大。

---

## class 與物件（看得懂即可）
```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id  # 建立物件屬性
```
```python
user.user_id  # 取用物件屬性
```
用途：自訂型別、封裝資料與行為，對應 PriorityQueue、attrgetter、namedtuple 等用法。

---

## 例外處理（try / except）
```python
try:
    int(val)  # 嘗試將 val 轉為整數
except ValueError:
    pass      # 若失敗則忽略錯誤
```
用途：處理輸入錯誤、資料驗證等，常見於 filter(is_int, values) 等情境。

---

## 基本 Big-O 觀念（聽得懂即可）
你需要知道：
- O(1)：常數時間，操作速度與資料量無關（如 dict 查找）
- O(N)：線性時間，操作速度與資料量成正比（如 for 迴圈）
- O(log N)：對數時間，常見於二分搜尋、heap 操作
用途：判斷程式效率、選擇合適資料結構與演算法。

- deque vs list
- heap push/pop
- sorted vs nlargest

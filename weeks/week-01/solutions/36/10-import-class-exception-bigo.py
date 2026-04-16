# 10-import-class-exception-bigo.py
# 範例：模組匯入、類別定義、例外處理與 Big-O 基礎

import heapq  # 內建 heapq 模組：用於優先佇列和堆積操作
from collections import deque  # deque 雙端佇列，適合從兩端快速新增/刪除

# 用戶類別範例
class User:
    def __init__(self, user_id):
        self.user_id = user_id  # 儲存使用者識別碼


user = User('u123')
print(f"User ID: {user.user_id}")  # 透過屬性讀取 user_id

# 例外處理範例
values = ['10', 'abc', '42']
for val in values:
    try:
        number = int(val)  # 可能會在非數字字串時拋出 ValueError
    except ValueError:
        print(f"無效數值：{val}")
    else:
        print(f"轉換成功：{number}")

# Big-O 概念說明：
# O(1) 常數時間，例如取列表元素
# O(N) 線性時間，例如遍歷列表
# O(log N) 對數時間，例如 heap 或二分搜尋

items = [5, 2, 9, 1, 7]
# deque vs list：deque 在左側新增/刪除更有效率
dq = deque(items)
dq.appendleft(0)
print(f"deque 左側新增後: {list(dq)}")

# heap push/pop：O(log N)
heap = []
for x in items:
    heapq.heappush(heap, x)
print(f"heap 最小值: {heapq.heappop(heap)}")

# sorted vs nlargest
print(f"排序後: {sorted(items)}")
print(f"前三大元素: {heapq.nlargest(3, items)}")

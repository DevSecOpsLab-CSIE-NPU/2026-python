# R3. deque 保留最後 N 筆（1.3）
# deque 是 Python collections 模組中的雙端隊列（double-ended queue），
# 它允許我們從序列的兩端高效地添加和移除元素。
# 與列表相比，deque 在頭部插入和刪除操作上更高效。

# 匯入 deque 類別
from collections import deque

# 創建一個 deque，設定最大長度為 3
# 當元素數量超過 maxlen 時，會自動移除最舊的元素
q = deque(maxlen=3)

# 向 deque 的右端添加元素
q.append(1); q.append(2); q.append(3)

# 再次添加元素 4，此時 deque 已經有 3 個元素，
# 所以會自動移除最舊的元素 1，保持長度為 3
q.append(4)  # 自動丟掉最舊的 1

# 創建一個沒有長度限制的 deque
q = deque()

# 向右端添加元素 1
q.append(1)

# 向左端添加元素 2，此時 deque 為 [2, 1]
q.appendleft(2)

# 從右端移除並返回元素（移除 1），deque 變為 [2]
q.pop()

# 從左端移除並返回元素（移除 2），deque 變為空 []
q.popleft()

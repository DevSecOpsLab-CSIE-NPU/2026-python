# R3. deque 保留最後 N 筆（Fixed-length deque）—— Python Cookbook 1.3

from collections import deque

# ── 固定大小的 deque（maxlen）────────────────────────────
# maxlen=3 表示最多保留 3 個元素
# 當超過時，最「舊」的那一端元素會自動被丟棄（先進先出）
q = deque(maxlen=3)
q.append(1)   # deque([1])
q.append(2)   # deque([1, 2])
q.append(3)   # deque([1, 2, 3])，已滿
q.append(4)   # deque([2, 3, 4])，1 被自動移除

# 使用場景：「滑動視窗」—— 例如保留最近 N 次的搜尋記錄、感測器讀值

# ── 沒有大小限制的 deque ─────────────────────────────────
# 可從兩端插入與刪除，時間複雜度均為 O(1)
# 比 list 的 insert(0, x) / pop(0) 快很多（list 是 O(n)）
q = deque()
q.append(1)      # 從右端插入 → deque([1])
q.appendleft(2)  # 從左端插入 → deque([2, 1])
q.pop()          # 從右端移除並回傳 → 移除 1，deque([2])
q.popleft()      # 從左端移除並回傳 → 移除 2，deque([])

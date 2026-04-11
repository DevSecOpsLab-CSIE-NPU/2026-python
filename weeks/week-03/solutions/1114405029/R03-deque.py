# R3. deque 保留最後 N 筆（1.3）

from collections import deque

# ── 1. 固定長度的環形緩衝區模式 ───────────────────────
# 建立一個最大長度為 3 的 deque
# 這是處理「最近紀錄」最優雅的方式，不需要手動檢查長度
q = deque(maxlen=3)

# 依序存入 1, 2, 3
q.append(1); q.append(2); q.append(3)
# 此時 q 為 deque([1, 2, 3], maxlen=3)

# 當加入第 4 個元素時，由於超過 maxlen=3
# deque 會自動從左側（最舊端）丟棄 1，將 4 加入右側
q.append(4)  # 自動丟掉最舊的 1
# 結果：q 為 deque([2, 3, 4], maxlen=3)

# ── 2. 雙向隊列的操作模式 ─────────────────────────────
# 建立一個不限長度的 deque（一般隊列模式）
q = deque()

# append(x)：從右側（末尾）加入元素
q.append(1)      # 狀態：[1]

# appendleft(x)：從左側（開頭）加入元素
# 注意：在標準 list 中執行此操作 (insert(0)) 效率很低，但在 deque 非常快
q.appendleft(2)  # 狀態：[2, 1]

# pop()：從右側（末尾）彈出並回傳元素
q.pop()          # 彈出 1，狀態：[2]

# popleft()：從左側（開頭）彈出並回傳元素
q.popleft()      # 彈出 2，狀態：[]
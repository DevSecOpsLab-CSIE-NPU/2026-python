# R3. deque 保留最後 N 筆（1.3）

from collections import deque

# 設定最大長度為 3，超出時會自動移除最舊資料
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

# 不設 maxlen 時可雙向操作
q = deque()
q.append(1); q.appendleft(2)
# pop 從右側取出；popleft 從左側取出
q.pop(); q.popleft()

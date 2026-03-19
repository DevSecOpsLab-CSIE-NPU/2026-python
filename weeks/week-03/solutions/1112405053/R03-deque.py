# R3. deque 保留最後 N 筆（1.3）

from collections import deque

# 設定最大長度 3，超過會自動丟掉最舊元素
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

# 也可當雙端佇列使用：左右都能進出
q = deque()
q.append(1); q.appendleft(2)
q.pop(); q.popleft()

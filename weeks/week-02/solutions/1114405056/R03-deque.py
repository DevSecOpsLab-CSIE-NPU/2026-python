# R3. deque 保留最後 N 筆（1.3）

from collections import deque

q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

q = deque()
q.append(1); q.appendleft(2)
q.pop(); q.popleft()

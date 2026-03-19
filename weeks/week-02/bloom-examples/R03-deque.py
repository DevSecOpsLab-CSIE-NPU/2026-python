"""R03: deque 雙端佇列範例。"""

from collections import deque

# maxlen=3 時，超出容量會自動淘汰最舊元素
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print('初始 q:', list(q))

q.append(4)
print('加入 4 後 (1 被淘汰):', list(q))

# 一般雙端操作
q2 = deque()
q2.append(1)
q2.appendleft(2)
print('q2 目前:', list(q2))
print('右側彈出:', q2.pop())
print('左側彈出:', q2.popleft())

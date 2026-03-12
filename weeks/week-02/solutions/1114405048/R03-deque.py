# R03 deque
# 目標：示範 collections.deque 在「固定長度緩衝區」與雙端操作的用途。

from collections import deque

# maxlen=3：超過長度時，自動丟掉最舊元素
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)  # 1 會被自動移除

# 雙端佇列可從左右兩側 push/pop
q = deque()
q.append(1)
q.appendleft(2)
q.pop()
q.popleft()

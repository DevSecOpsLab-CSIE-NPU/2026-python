# R3. deque 保留最後 N 筆（1.3）

from collections import deque

# maxlen=3：只保留最後 3 筆
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)  # 自動丟掉最舊的 1
print('固定長度 deque:', list(q))

# 不限制長度時，可在左右兩端推入/彈出
q = deque()
q.append(1)
q.appendleft(2)
right_value = q.pop()
left_value = q.popleft()
print('從右側取出:', right_value)
print('從左側取出:', left_value)
print('目前 deque 內容:', list(q))

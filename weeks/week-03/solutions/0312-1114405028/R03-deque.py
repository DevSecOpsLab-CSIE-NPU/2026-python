# R3. deque 保留最後 N 筆（1.3）
# deque 可設定 maxlen，自動在尾部丟棄最舊元素。

from collections import deque

print("---- 限長 deque 範例 ----")
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
print("initial deque", q)
q.append(4)  # 自動丟掉最舊的 1
print("after appending 4", q)

print("---- 一般 deque 操作 ----")
q = deque()
q.append(1); q.appendleft(2)
print("after append/appendleft", q)
print("pop returns", q.pop())
print("popleft returns", q.popleft())


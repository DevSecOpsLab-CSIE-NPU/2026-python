"""
R03: deque（雙端佇列）

deque 適合在「頭尾兩端」都需要高效率插入/移除的場景。
"""

from collections import deque

# 指定 maxlen=3 後，deque 會自動維持最多 3 筆。
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

# 再加入 4 時，最左邊（最舊）的 1 會被自動移除。
q.append(4)

# 不限制長度時，可同時示範左右兩端操作。
q = deque()
q.append(1)       # 右側加入
q.appendleft(2)   # 左側加入
q.pop()           # 右側移除
q.popleft()       # 左側移除

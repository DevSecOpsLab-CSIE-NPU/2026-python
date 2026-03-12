# R3: deque（雙端佇列）
# 觀念：deque 可以在頭尾都做 O(1) 的插入/刪除，適合佇列與滑動視窗。

from collections import deque

# 設定最大長度 3：超過時會自動丟掉最舊（左邊）元素
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)  # 變成 deque([2, 3, 4], maxlen=3)

# 不限制長度時，可自由從左右兩端操作
q = deque()
q.append(1)      # 右側加入 -> deque([1])
q.appendleft(2)  # 左側加入 -> deque([2, 1])
q.pop()          # 右側移除，回傳 1
q.popleft()      # 左側移除，回傳 2

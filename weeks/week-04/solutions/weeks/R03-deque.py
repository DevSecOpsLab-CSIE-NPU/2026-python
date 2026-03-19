# R3. deque 保留最後 N 筆（1.3）

from collections import deque

# 建立一個 deque，最多只保留 3 個元素
q = deque(maxlen=3)

# 依序加入元素，deque 會保持先進先出（FIFO）
q.append(1)
q.append(2)
q.append(3)

# 再加入第 4 個元素時，因為 maxlen=3
# 最舊的元素 1 會自動被丟棄
q.append(4)  # 自動丟掉最舊的 1

# 建立一個沒有長度限制的 deque
q = deque()

# append() 從右邊加入；appendleft() 從左邊加入
q.append(1)        # 右邊加入 1 → deque: [1]
q.appendleft(2)    # 左邊加入 2 → deque: [2, 1]

# pop() 從右邊彈出；popleft() 從左邊彈出
q.pop()            # 彈出右邊的 1 → deque: [2]
q.popleft()        # 彈出左邊的 2 → deque: []
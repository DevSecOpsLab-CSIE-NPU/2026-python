"""R3. deque 保留最後 N 筆（1.3）

deque 是 collections 模組提供的雙向佇列：
1. 可以從左邊或右邊快速加入 / 移除元素。
2. 常用於隊列、滑動視窗、保留最近 N 筆資料。
3. 搭配 maxlen 時，超過容量的舊資料會自動被丟棄。
"""

from collections import deque

# 建立一個最多只保留 3 筆資料的 deque
q = deque(maxlen=3)
# append() 從右邊加入元素
q.append(1); q.append(2); q.append(3)
# 當容量滿了再 append，新元素會進來，最舊的元素會被自動移除
q.append(4)  # 自動丟掉最舊的 1

# 沒有設定 maxlen 時，deque 就像一般可雙向操作的容器
q = deque()
# appendleft() 從左邊加入元素，和 append() 的方向相反
q.append(1); q.appendleft(2)
# pop() 從右邊移除最後一個元素
# popleft() 從左邊移除第一個元素
q.pop(); q.popleft()

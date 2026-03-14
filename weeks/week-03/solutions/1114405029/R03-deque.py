# R3. deque 保留最後 N 筆（1.3）
#
# deque（double-ended queue）是「雙端佇列」：
# - 可在左右兩端快速新增/刪除元素。
# - 很適合做「滑動視窗」、「最近 N 筆資料」等情境。

from collections import deque

# 1) 設定固定容量 maxlen=3：只保留最新 3 筆
q = deque(maxlen=3)

# 依序加入 1, 2, 3
# 此時 q = deque([1, 2, 3], maxlen=3)
q.append(1); q.append(2); q.append(3)

# 再加入 4 時，因為容量滿了，會自動移除最左邊（最舊）的元素 1
# 結果 q = deque([2, 3, 4], maxlen=3)
q.append(4)  # 自動丟掉最舊的 1


# 2) 不設定 maxlen：容量可成長
q = deque()

# append(x)：從右邊加入
# appendleft(x)：從左邊加入
# 先 append(1) 後 appendleft(2)，結果 q = deque([2, 1])
q.append(1); q.appendleft(2)

# pop()：移除並回傳右邊元素（這裡會拿到 1）
# popleft()：移除並回傳左邊元素（這裡會拿到 2）
# 兩次後 q 會變成空的 deque([])
q.pop(); q.popleft()


# 讀懂這段程式的關鍵思路：
# 1. 把 deque 想成「左右都能進出」的容器，而不是只能尾端操作的 list。
# 2. 有 maxlen 時，新增新資料可能觸發自動淘汰最舊資料。
# 3. 觀察每一步是「從左」還是「從右」操作，腦中就能追出最終內容。
# 4. 若你需要固定記憶體、只保留最近資料，deque(maxlen=N) 通常比手動切 list 更直觀。

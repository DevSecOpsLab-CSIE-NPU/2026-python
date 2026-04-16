# R3. deque 保留最後 N 筆（1.3）
#
# collections.deque 適合做雙端佇列：
# 1. append / pop 都很快，適合需要在左右兩端操作的情境。
# 2. maxlen 可以限制長度，超過時會自動丟掉最舊的資料。
# 3. 很適合拿來記錄最近 N 筆資料，例如近期紀錄、歷史輸入。

from collections import deque

q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

q = deque()
q.append(1); q.appendleft(2)
q.pop(); q.popleft()

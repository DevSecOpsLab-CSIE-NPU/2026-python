# U03 deque(maxlen=N) 的固定長度行為
# 重點：超過長度上限時，最舊資料會自動被丟棄。

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 最終只保留最新的 3 筆資料：[3, 4, 5]

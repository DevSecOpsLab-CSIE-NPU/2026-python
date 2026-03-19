# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
# 結果只剩 [3, 4, 5]

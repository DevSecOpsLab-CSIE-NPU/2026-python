"""U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

deque 在達到 maxlen 時會自動從左側丟棄最舊的元素，因此會保留最後的 N 筆。
"""

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
# 結果只剩 [3, 4, 5] 

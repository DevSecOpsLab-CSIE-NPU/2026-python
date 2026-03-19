"""
U03: deque 的 maxlen

當長度超過上限時，最舊的資料會自動被移除。
"""

from collections import deque


q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 最後只會保留最近加入的 3 個值。
# 內容會是 [3, 4, 5]

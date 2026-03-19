# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

from collections import deque  # deque：雙端佇列，支援 O(1) 的兩端常數時間增刪

q = deque(maxlen=3)  # 設定容量上限為 3
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    # append 時若佇列已滿，自動從左端移除最舊的元素
    # 這就是「滑動視窗」（sliding window）的底層實作原理
# 結果只剩 [3, 4, 5]：保留最後沿入的 3 個元素

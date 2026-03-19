# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
#
# 觀念重點：
# - deque 設定 maxlen 後，超出容量時會自動丟掉「最舊」資料。
# - 很適合做固定長度的最近紀錄（例如最近 N 次操作）。

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    # 當 append 第 4、5 筆時，左側舊資料會被自動移除。

# 最後只保留最近 3 筆：deque([3, 4, 5], maxlen=3)
print(q)
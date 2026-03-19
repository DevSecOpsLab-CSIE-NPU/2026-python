# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
"""
本範例示範 collections.deque 的 maxlen 參數如何自動維持固定長度的「環形緩衝區」。

當 deque 的長度達到 maxlen 時，再 append 新元素會自動從左側（最舊的元素）
彈出一個元素，確保 deque 只保留最近的 N 筆資料。

常見用途：
- 追蹤最近 N 筆事件、紀錄最近的操作歷史
- 實作滑動視窗（sliding window）或簡易的 FIFO 緩衝區
"""

from collections import deque

# 建立一個最大只能放 3 筆資料的 deque
q = deque(maxlen=3)

# 依序 append 數字 1~5
# 當 append 到第 4 個元素時，deque 內已有 3 筆元素，
# 會自動把最舊的 1 彈出，維持長度不超過 maxlen
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 最後只會留下最新的三筆： [3, 4, 5]
# 這就是 maxlen 行為的關鍵：永遠保留最後 N 筆資料


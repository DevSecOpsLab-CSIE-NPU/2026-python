# 【Bloom 階段：R - 記憶與基本操作】
# R3. 使用 deque 維持最後 N 筆記錄
# August 的惡意提醒：這是 Big-O 觀念的實作。
# 在 Week 06 處理流式資料時，如果你用 list.pop(0)，你的時間複雜度會變 O(N)。
# 使用 deque 能保證兩端操作都是 O(1)。

from collections import deque

# 設定最大長度的隊列，適合用來實作「最近瀏覽紀錄」
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 隊列已滿，自動從另一頭丟掉 1

# 一般隊列操作
q = deque()
q.append(1)         # 從右邊進
q.appendleft(2)     # 從左邊進 (O(1))
val = q.pop()       # 從右邊出
val_left = q.popleft()  # 從左邊出 (O(1))

print(f"Final queue: {list(q)}")

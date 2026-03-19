# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
#
# collections.deque 可以設定 maxlen，讓雙端佇列維持固定長度。
# 當新增元素使長度超過 maxlen 時，deque 會自動從另一端丟棄最舊的元素。
# 這種行為適合用於「最新 N 筆資料」的緩衝區或歷史紀錄。

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
# 結果只剩 [3, 4, 5]

print(q)

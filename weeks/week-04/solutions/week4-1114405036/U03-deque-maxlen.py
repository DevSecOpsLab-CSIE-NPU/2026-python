# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
# 說明：當 deque 設定了 maxlen 且滿了時，加入新元素會自動從另一端移除舊元素。

from collections import deque

# 建立一個最多只能存 3 個元素的隊列
q = deque(maxlen=3)

for i in [1, 2, 3, 4, 5]:
    q.append(i)
    print(f"目前隊列內容: {list(q)}")

# 最終結果只剩 [3, 4, 5]，因為 1 和 2 被「推」出去了
# 這在實作「最近 N 筆歷史紀錄」的功能時非常有用。
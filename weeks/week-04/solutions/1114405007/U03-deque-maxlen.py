# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

from collections import deque

# 建立最多只保留 3 筆資料的雙端佇列
q = deque(maxlen=3)

# 當資料超過上限時，左邊較舊的元素會自動被丟掉
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 結果只剩 [3, 4, 5]
print('deque 內容:', list(q))

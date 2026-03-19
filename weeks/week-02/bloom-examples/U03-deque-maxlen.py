"""U03: deque(maxlen=N) 會自動維持固定長度。"""

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    print(f'append({i}) ->', list(q))

print('最終結果只保留最後 3 個:', list(q))

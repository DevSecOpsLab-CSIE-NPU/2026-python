# 11150 最簡單版本 - 青蛙過橋
from collections import deque

while True:
    L, S, T, M = map(int, input().split())
    if L == S == T == M == 0: break
    
    stones = set(map(int, input().split())) if M > 0 else set()
    
    q = deque([(0, 0)])
    v = {0: 0}
    ans = float('inf')
    
    while q:
        pos, cnt = q.popleft()
        if pos + S >= L:
            ans = min(ans, cnt)
            continue
        
        for j in range(S, T + 1):
            nxt = pos + j
            if nxt >= L:
                ans = min(ans, cnt)
            else:
                nc = cnt + (nxt in stones)
                if nxt not in v or v[nxt] > nc:
                    v[nxt] = nc
                    q.append((nxt, nc))
    
    print(ans)

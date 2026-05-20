# 11321 最簡單版本 - 魔法路
from collections import deque

def can_go(N, M, traps):
    g = {(x, y) for x, y in traps}
    q = deque((x, 0) for x in range(N) if (x, 0) not in g)
    v = set(q)
    
    while q:
        x, y = q.popleft()
        if y == M - 1: return True
        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in v and (nx,ny) not in g:
                v.add((nx, ny))
                q.append((nx, ny))
    return False

while True:
    N, M, T = map(int, input().split())
    if N == M == T == 0: break
    
    traps = set()
    for _ in range(T):
        x, y = map(int, input().split())
        if can_go(N, M, traps | {(x, y)}):
            print("<(_ _)>")
            traps.add((x, y))
        else:
            print(">_<")

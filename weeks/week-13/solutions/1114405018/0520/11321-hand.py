import sys
from collections import deque

def can_reach_right(N, M, blocked):
    q = deque()
    seen = [[False]*M for _ in range(N)]
    for r in range(N):
        if not blocked[r][0]:
            q.append((r,0)); seen[r][0]=True
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y = q.popleft()
        if y == M-1:
            return True
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not blocked[nx][ny] and not seen[nx][ny]:
                seen[nx][ny]=True; q.append((nx,ny))
    return False

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    it = iter(data)
    N = next(it); M = next(it); T = next(it)
    blocked = [[False]*M for _ in range(N)]
    out = []
    for _ in range(T):
        x = next(it); y = next(it)
        if blocked[x][y]:
            out.append("<_(_ _)>")
            continue
        blocked[x][y] = True
        if can_reach_right(N, M, blocked):
            out.append("<(_ _)>")
        else:
            out.append(">_<")
            blocked[x][y] = False
    print("\n".join(out))

if __name__ == '__main__':
    solve()
    
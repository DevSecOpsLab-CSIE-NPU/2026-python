import sys
from collections import deque

def solve():
    data = sys.stdin.read().splitlines()
    N, M, T = map(int, data[0].split())
    traps = [tuple(map(int, line.split())) for line in data[1:1+T]]
    blocked = set()
    out = []

    for x, y in traps:
        blocked.add((x, y))
        q = deque()
        seen = [[False]*M for _ in range(N)]
        for r in range(N):
            if (r, 0) not in blocked:
                q.append((r, 0))
                seen[r][0] = True
        ok = False
        while q and not ok:
            cx, cy = q.popleft()
            if cy == M-1:
                ok = True
                break
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < N and 0 <= ny < M and not seen[nx][ny] and (nx, ny) not in blocked:
                    seen[nx][ny] = True
                    q.append((nx, ny))
        if ok:
            out.append("<(_ _)>")
        else:
            blocked.remove((x, y))
            out.append(">_<")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

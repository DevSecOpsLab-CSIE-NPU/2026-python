import sys
from collections import deque

def has_path(N, M, blocked):
    """
    BFS 檢查從左側（任意行）是否能走到右側（最後一列）。
    blocked 為已放置陷阱的座標集合。
    """
    visited = set()
    q = deque()
    # 從左側所有非陷阱起點出發
    for i in range(N):
        if (i, 0) not in blocked:
            q.append((i, 0))
            visited.add((i, 0))
    while q:
        x, y = q.popleft()
        if y == M - 1:          # 到達右側終點
            return True
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in blocked and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return False

def can_place(N, M, traps):
    """
    依序檢查每個陷阱可否放置。
    若放置後導致無路可到終點，則拒絕該陷阱。
    """
    results = []
    blocked = set()
    for x, y in traps:
        blocked.add((x, y))
        if not has_path(N, M, blocked):
            blocked.remove((x, y))   # 不放該陷阱
            results.append(False)
        else:
            results.append(True)
    return results

def solve(data=None):
    """讀取輸入、計算並回傳結果"""
    if data is None:
        data = sys.stdin.read()
    lines = data.strip().splitlines()
    N, M, T = map(int, lines[0].split())
    traps = []
    for i in range(1, T+1):
        x, y = map(int, lines[i].split())
        traps.append((x, y))
    results = can_place(N, M, traps)
    out = "\n".join("<(_ _)>" if r else ">_<" for r in results) + "\n"
    return out

if __name__ == "__main__":
    sys.stdout.write(solve())

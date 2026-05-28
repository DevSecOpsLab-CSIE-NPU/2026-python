"""UVA 11321 - 判斷放陷阱是否會封路

每次嘗試放一個陷阱，若放置後會導致左側無法連到右側，則不放並輸出 ">_<"，
否則放置並輸出 "<(_ _)>"。
"""

from __future__ import annotations

import sys
from collections import deque


def is_connected(N: int, M: int, blocked: list[list[bool]]) -> bool:
    # BFS 從所有未被封鎖的左側格子出發，檢查是否能到任何右側未封鎖格子
    q = deque()
    vis = [[False] * M for _ in range(N)]
    for i in range(N):
        if not blocked[i][0]:
            q.append((i, 0))
            vis[i][0] = True

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y = q.popleft()
        if y == M-1:
            return True
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and (not blocked[nx][ny]) and (not vis[nx][ny]):
                vis[nx][ny] = True
                q.append((nx, ny))

    return False


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    idx = 0
    N = data[idx]; M = data[idx+1]; T = data[idx+2]
    idx += 3
    blocked = [[False]*M for _ in range(N)]
    outputs: list[str] = []
    for _ in range(T):
        x = data[idx]; y = data[idx+1]
        idx += 2
        # 座標系統左下角 (0,0)，x 是縱軸 (row)，y 是橫軸 (col)
        # 但我們的陣列以 0..N-1 自上而下或自下而上都可，因為 BFS 不受影響
        # 這裡就直接用 x as row index
        if blocked[x][y]:
            outputs.append("<_(_ _)>" )
            continue

        # 暫時放置陷阱
        blocked[x][y] = True
        if is_connected(N, M, blocked):
            outputs.append("<(_ _)>")
            # keep the trap
        else:
            outputs.append(">_<")
            blocked[x][y] = False

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()

"""
Problem 11321 - 放陷阱（判斷放陷阱是否會封死路）

實作說明：
- 使用一個布林矩陣 `blocked` 來記錄目前已放置的陷阱位置。
- 每次要放置一個陷阱時，暫時把該格標為 blocked，然後從左邊所有未被封住的格子做 BFS，看是否能到達右邊任一格。
- 若仍存在路徑，則真正放置該陷阱並輸出成功；否則還原並輸出失敗。

此檔提供 `process(input_str)` 以便 unit test 使用，並包含必要的繁體中文註解。
"""

from collections import deque
from typing import List


def can_reach_right(N: int, M: int, blocked: List[List[bool]]) -> bool:
    """從左側未封格做 BFS，檢查是否能到達右側任一格。"""
    visited = [[False] * M for _ in range(N)]
    dq = deque()
    # 左邊縱列 col = 0
    for r in range(N):
        if not blocked[r][0]:
            dq.append((r, 0))
            visited[r][0] = True

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while dq:
        r, c = dq.popleft()
        if c == M - 1:
            return True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not blocked[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr, nc))
    return False


def process(input_str: str) -> str:
    """解析輸入，對每個要放的陷阱輸出是否可放。

    輸入格式：第一行 N M T，接著 T 行每行 x y。
    座標系：左下角為 (0,0)，x 為縱軸（0..N-1），y 為橫軸（0..M-1）。
    輸出：對每個陷阱輸出一行："<(_ _)>" (可放) 或 ">_<" (不可放)。
    """
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    N = int(tokens[p]); p += 1
    M = int(tokens[p]); p += 1
    T = int(tokens[p]); p += 1

    # 初始化 blocked 矩陣（False 表示可通行）
    blocked = [[False] * M for _ in range(N)]
    out_lines: List[str] = []

    for _ in range(T):
        x = int(tokens[p]); y = int(tokens[p+1]); p += 2
        # 轉為 (r,c)；此題座標原點在左下，但對 BFS 不影響方向，只要一致即可
        r, c = x, y

        # 先暫時放置陷阱
        blocked[r][c] = True
        if can_reach_right(N, M, blocked):
            out_lines.append("<(_ _)>")
            # 保留 blocked[r][c] = True
        else:
            out_lines.append(">_<")
            # 還原為未放置
            blocked[r][c] = False

    return "\n".join(out_lines)


def main():
    import sys
    print(process(sys.stdin.read()))


if __name__ == '__main__':
    main()

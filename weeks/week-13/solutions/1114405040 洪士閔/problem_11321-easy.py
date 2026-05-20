"""
簡易版 Problem 11321（放陷阱）— 詳細註解版

問題回顧：在 N x M 的網格上依序放置陷阱，每次放置前必須檢查放置後是否仍保有從左邊任一格到右邊任一格的通路。

演算法要點：
- 每次放置先暫時標記該格為阻塞（blocked），呼叫 BFS 檢查是否存在從左列任一未封格到達右列任一格的路徑。
- 若 BFS 回傳 True（仍有路），則保留該阻塞；否則還原，表示放置失敗。

此簡易版程式以清晰步驟與註解說明 BFS 的建立與啟點，方便手寫與教學。
"""

from collections import deque
from typing import List


def can_reach_right(N: int, M: int, blocked: List[List[bool]]) -> bool:
    """從左側未封的格子啟始 BFS，檢查是否能到達右側任一格。

    實作細節：
    - 使用 visited 以避免重覆搜尋。
    - BFS 的起點為所有 col=0（左邊）且未被 blocked 的格子。
    - 若在搜尋過程中有任何節點的 c == M-1（右邊），代表存在可達路徑。
    - 回傳布林值表示是否可達。
    """
    visited = [[False] * M for _ in range(N)]
    dq = deque()
    # 把左邊所有可走的格子當作 BFS 起點
    for r in range(N):
        if not blocked[r][0]:
            dq.append((r, 0))
            visited[r][0] = True
    # 四個方向（上下左右）
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        r, c = dq.popleft()
        # 一旦到達右邊任一格即成功
        if c == M-1:
            return True
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not blocked[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr, nc))
    return False


def process(input_str: str) -> str:
    """解析輸入並對每個要放置的座標輸出是否放置成功。

    輸入格式：N M T，接著 T 組 x y 座標。座標原點在左下，但在本實作中我們只要一致地把 x 當作列 r，y 當作欄 c 即可。
    回傳值：每次嘗試放置輸出一行，成功為 `<(_ _)>`，失敗（封死路徑）為 `>_<`。
    """
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    N = int(tokens[p]); p += 1
    M = int(tokens[p]); p += 1
    T = int(tokens[p]); p += 1
    blocked = [[False]*M for _ in range(N)]
    out_lines: List[str] = []
    for _ in range(T):
        x = int(tokens[p]); y = int(tokens[p+1]); p += 2
        r, c = x, y
        # 暫時放置，測試是否會封死
        blocked[r][c] = True
        if can_reach_right(N, M, blocked):
            out_lines.append("<(_ _)>")
            # 保留 blocked[r][c] = True
        else:
            out_lines.append(">_<")
            # 還原為未放置
            blocked[r][c] = False
    return "\n".join(out_lines)


if __name__ == '__main__':
    import sys
    print(process(sys.stdin.read()))

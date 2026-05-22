"""
UVA 11321 簡易解題模組（教學 / 單元測試用）

說明：題目要求依序嘗試在格子上放置陷阱，若放下該陷阱會導致從左邊任一格(不為陷阱)無法到達右邊任一格(不為陷阱)，則不得放置。
本模組提供一個直觀且能通過小到中等尺寸測資的實作：每次嘗試放置陷阱後，使用 BFS 檢查是否仍存在從左邊到右邊的路徑；若存在則接受該陷阱，否則還原並拒絕。

注意：此實作為 -easy/教學版，對極大格子（如 N,M 達數千或更高）可能效能不足；進階作法可使用動態聯通性或倒向處理 (reverse processing)／座標壓縮等。
"""

from typing import List, Tuple
from collections import deque


def path_exists(grid: List[List[int]]) -> bool:
    """
    判斷在目前 grid（0: 可通行；1: 陷阱）下，是否存在從左邊任一可通行格子到右邊任一可通行格子的路徑。
    使用四方向 BFS（上下左右）。
    """
    if not grid or not grid[0]:
        return False
    N = len(grid)
    M = len(grid[0])
    visited = [[False] * M for _ in range(N)]
    dq = deque()

    # 將左邊邊界所有可通行格子加入 BFS 起點
    for x in range(N):
        if grid[x][0] == 0:
            visited[x][0] = True
            dq.append((x, 0))

    while dq:
        x, y = dq.popleft()
        # 如果到達右邊邊界，代表存在路徑
        if y == M - 1:
            return True
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                dq.append((nx, ny))

    return False


def simulate_trap_sequence(N: int, M: int, proposals: List[Tuple[int, int]]) -> List[str]:
    """
    模擬依序提出的陷阱位置 proposals（List[(x,y)]），對每一個位置回傳字串結果：
    - '<(_ _)>' 表示該陷阱可放（放下之後仍有路徑）
    - '>_<' 表示該陷阱不可放（放下會封死道路），不會把該陷阱放上去

    傳回的結果串列長度等於 proposals 長度，且順序對應。
    """
    # 建立空格子地圖：0 可通行，1 陷阱
    grid = [[0] * M for _ in range(N)]
    outputs: List[str] = []

    for x, y in proposals:
        # 保險檢查：若該點已經是陷阱（題目保證不會重覆），視為不可放
        if grid[x][y] == 1:
            outputs.append('>_<')
            continue

        # 嘗試放置陷阱
        grid[x][y] = 1
        if path_exists(grid):
            outputs.append('<(_ _)>')
            # 保持陷阱
        else:
            outputs.append('>_<')
            # 還原，不放置
            grid[x][y] = 0

    return outputs


def parse_and_run_stdin() -> None:
    """
    從標準輸入讀取題目格式的輸入並輸出結果，每一行輸出 '<(_ _)>' 或 '>_<'。

    輸入格式：
    N M T
    x1 y1
    x2 y2
    ... (共 T 行)
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        N = int(next(it))
        M = int(next(it))
        T = int(next(it))
    except StopIteration:
        return

    proposals = []
    for _ in range(T):
        try:
            x = int(next(it)); y = int(next(it))
        except StopIteration:
            break
        proposals.append((x, y))

    results = simulate_trap_sequence(N, M, proposals)
    out = '\n'.join(results)
    if out:
        print(out)


if __name__ == '__main__':
    # 若以管道或檔案方式提供 stdin，解析並執行；否則執行簡單範例
    import sys
    if sys.stdin.isatty():
        N = 3
        M = 3
        proposals = [(0, 1), (1, 1), (2, 1)]
        print(simulate_trap_sequence(N, M, proposals))
    else:
        parse_and_run_stdin()

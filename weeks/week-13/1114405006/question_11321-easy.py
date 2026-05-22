"""
極簡易版（-easy）：UVA 11321 的直觀實作，適合教學與小型測資。

詳盡說明（繁體中文）：

- 題目要點：在 N x M 的格子道路上，依序嘗試放置 T 個陷阱（座標給定），
    若放置某個陷阱會使得「從任一左邊邊界的可通行格子」皆無法到達「任一右邊邊界的可通行格子」，
    則該陷阱不得放置；否則可以放置。

- 直觀做法（此檔實作）：
    1. 使用二維陣列 `grid` 表示地圖：`0` 可通行、`1` 為陷阱。初始皆為 0。
    2. 對每一個提案 (x, y)：
         a. 若該格已是陷阱，直接回傳拒絕 `>_<`（題目保證不重複提案，此處為保險）。
         b. 暫時把該格設為陷阱（grid[x][y] = 1）。
         c. 從左邊邊界所有可通行格子出發做 BFS（四方向：上下左右），檢查是否能抵達右邊邊界的任一格。
         d. 若能到，則接受該陷阱（回傳 '<(_ _)>'）；否則還原該格為 0 並回傳 '>_<'。

- 為何可行：只要驗證放置該陷阱後是否仍存在左邊到右邊的路徑即可，而 BFS 能在 O(N*M) 內找出是否存在任一路徑。

- 限制與優化方向：
    - 本實作每個提案都會跑一次 BFS，若 T 很大或 N*M 很大，總時間 O(T*N*M) 可能太慢。
    - 進階作法可採「逆序處理 + 聯通塊 (DSU)」或動態維護連通性，以達到較佳效能。

- 輸入／輸出：
    - 輸入（stdin）：
            N M T
            x1 y1
            x2 y2
            ...
    - 輸出（stdout）：每一行對應一個提案，輸出 '<(_ _)>'（接受）或 '>_<'（拒絕）。

範例使用：
    python question_11321-easy.py < input.txt

此檔刻意保持程式結構簡潔、敘述直觀，方便教學與人工閱讀。
"""

from collections import deque
from typing import List, Tuple


def simulate_traps_easy(N: int, M: int, proposals: List[Tuple[int, int]]) -> List[str]:
    """
    簡潔直觀的處理流程：對每個提案嘗試放置陷阱，並用 BFS 驗證是否仍有左->右的路徑。

    參數：
    - N, M: 地圖大小（N 列、M 行）
    - proposals: 提案位置清單 [(x,y), ...]

    回傳：每個提案的結果字串列表（'<(_ _)>' 或 '>_<')
    """
    # 建立地圖（0: 可走，1: 陷阱）
    grid: List[List[int]] = [[0] * M for _ in range(N)]
    results: List[str] = []

    for x, y in proposals:
        # 保險檢查：若該格已為陷阱則直接拒絕
        if grid[x][y] == 1:
            results.append('>_<')
            continue

        # 暫時放置陷阱
        grid[x][y] = 1

        # BFS 初始：將左邊邊界所有可通行格子加入佇列
        q = deque()
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            if grid[i][0] == 0:
                visited[i][0] = True
                q.append((i, 0))

        # BFS 搜尋是否能達到右邊邊界
        found = False
        while q:
            i, j = q.popleft()
            if j == M - 1:
                found = True
                break
            # 四個方向
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))

        if found:
            results.append('<(_ _)>')
        else:
            # 若找不到路徑，還原該格
            results.append('>_<')
            grid[x][y] = 0

    return results


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); M = int(next(it)); T = int(next(it))
    proposals = []
    for _ in range(T):
        x = int(next(it)); y = int(next(it))
        proposals.append((x, y))

    for line in simulate_traps_easy(N, M, proposals):
        print(line)


if __name__ == '__main__':
    main()

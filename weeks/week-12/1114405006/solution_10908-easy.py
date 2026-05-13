"""
10908 簡易版實作（含繁體中文詳細註解）

簡短說明：
本檔為題目 10908（Largest Square）的簡易、好記版本。
思路為：以中心位置 (r, c) 為基準，向外擴張可能的半徑 k，
每次只檢查新增的外框是否全部與中心字元相同，若不相同則停止。
回傳最大邊長（odd number），即 2*k + 1。

此檔刻意寫得簡潔同時補上清楚註解，方便在考試或面試中快速寫出來。
"""


def largest_square(grid, r, c):
    """計算以 (r, c) 為中心的最大同字元正方形邊長（必為奇數）。

    參數：
    - grid: 二維清單（每個元素為一行字元列表）
    - r, c: 中心座標（0-based）

    回傳：
    - 最大正方形邊長（int），如果 grid 為空或座標錯誤則回傳 0

    演算法說明（重點）：
    1. 先處理防護情況（空格、錯誤座標）
    2. 以中心字元 `ch` 為基準，計算可能的最大半徑 `max_k`，
       這由距離四邊界的最小值決定
    3. 從 k=0 開始（邊長 1），逐步嘗試擴張到 k+1：
       - 檢查新擴張外框（上邊、下邊、左邊、右邊）是否全部等於 `ch`
       - 若有任一格不等，代表不能再擴張，結束迴圈
    4. 回傳 2*k + 1

    時間複雜度：每次擴張檢查外框長度 O(k)，總體約 O(k^2) 但實務上通常小。
    """
    # 防護：如果 grid 為空，直接回傳 0
    if not grid:
        return 0

    M = len(grid)
    N = len(grid[0])

    # 防護：座標若超出範圍，則視為無效
    if r < 0 or r >= M or c < 0 or c >= N:
        return 0

    # 中心字元
    ch = grid[r][c]

    # 最大可能半徑：受上下左右邊界限制
    max_k = min(r, c, M - 1 - r, N - 1 - c)

    # k = 0（邊長 1）一定成立，從這裡開始嘗試擴張
    k = 0
    while k < max_k:
        nk = k + 1  # 嘗試擴張後的半徑

        # 檢查上邊與下邊的整段（從 c-nk 到 c+nk）
        ok = True
        for j in range(c - nk, c + nk + 1):
            if grid[r - nk][j] != ch or grid[r + nk][j] != ch:
                ok = False
                break

        if not ok:
            break

        # 檢查左右邊（除了上下角落已被上面檢查過）
        for i in range(r - nk + 1, r + nk):
            if grid[i][c - nk] != ch or grid[i][c + nk] != ch:
                ok = False
                break

        if not ok:
            break

        # 如果外框皆相同，正式將半徑增加
        k = nk

    # 回傳邊長（2*k + 1）
    return 2 * k + 1


if __name__ == '__main__':
    # 簡單 CLI（僅供手動測試）
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)

    it = iter(data)
    T = int(next(it))
    out = []

    for _ in range(T):
        M = int(next(it)); N = int(next(it)); Q = int(next(it))
        # 讀取 M 行，每行為寬為 N 的字元字串
        grid = [list(next(it).rstrip()) for _ in range(M)]
        for _ in range(Q):
            r = int(next(it)); c = int(next(it))
            out.append(str(largest_square(grid, r, c)))

    sys.stdout.write('\n'.join(out))

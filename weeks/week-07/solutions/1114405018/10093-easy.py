from functools import lru_cache
import sys


def generate_row_states(m):
    """產生單列所有合法狀態。

    狀態用 bitmask 表示：
    - 例如 m=5 時，狀態 0b10010 表示第 2、5 欄有放炮兵。
    - bit=1 代表該欄放了炮兵。

    同一列的限制：
    - 不能在相鄰欄位同時放（距離 1）
    - 不能在隔一格欄位同時放（距離 2）
    """
    states = []
    for s in range(1 << m):
        # 若 s 與左移 1 位有重疊，代表有相鄰兩欄同時放置
        if s & (s << 1):
            continue
        # 若 s 與左移 2 位有重疊，代表有距離 2 的衝突
        if s & (s << 2):
            continue
        states.append(s)
    return states


def max_artillery(grid):
    """回傳最多可部署炮兵數量。

    easy 記法：
    1. 每一列先列舉所有「列內合法」狀態。
    2. 用 DFS + 記憶化決定每一列放法。
    3. DFS 狀態只記三件事：目前列 i、上一列狀態、上上列狀態。

    為什麼只需要看前兩列：
    - 題目的縱向攻擊距離是 2。
    - 所以第 i 列只會被 i-1 與 i-2 影響，不需看更遠列。
    """
    n = len(grid)
    if n == 0:
        return 0

    m = len(grid[0])

    # states: 單列合法狀態清單
    states = generate_row_states(m)

    # cnt[k]: 狀態 states[k] 這一列放了幾支炮兵（bit 數量）
    cnt = [s.bit_count() for s in states]

    # blocked[i] 的 bit=1 代表該格是 H（山地）不能放炮兵
    blocked = []
    for row in grid:
        mask = 0
        for j, ch in enumerate(row):
            if ch == "H":
                mask |= 1 << j
        blocked.append(mask)

    # row_candidates[i]: 第 i 列可用的狀態索引（不踩到山地）
    # 先過濾可大幅減少 DFS 分支數。
    row_candidates = []
    for i in range(n):
        cands = []
        for idx, s in enumerate(states):
            if (s & blocked[i]) == 0:
                cands.append(idx)
        row_candidates.append(cands)

    # 空狀態（整列不放）作為邊界初始化用
    zero_idx = states.index(0)

    @lru_cache(maxsize=None)
    def dfs(i, prev1_idx, prev2_idx):
        """回傳從第 i 列開始到最後一列，最多還能放多少炮兵。

        參數:
        - i: 目前要決定的列索引
        - prev1_idx: 第 i-1 列使用的狀態索引
        - prev2_idx: 第 i-2 列使用的狀態索引
        """
        if i == n:
            # 所有列都處理完，後續可放數量為 0
            return 0

        best = 0
        prev1 = states[prev1_idx]
        prev2 = states[prev2_idx]

        for cur_idx in row_candidates[i]:
            cur = states[cur_idx]

            # 垂直距離 1：不能同欄
            if cur & prev1:
                continue

            # 垂直距離 2：不能同欄
            if cur & prev2:
                continue

            # 選擇目前狀態後，遞迴處理下一列
            best = max(best, cnt[cur_idx] + dfs(i + 1, cur_idx, prev1_idx))

        return best

    # 從第 0 列開始，且前兩列視為空狀態
    return dfs(0, zero_idx, zero_idx)


def solve(text):
    """讀入整段輸入字串，回傳答案字串。"""

    parts = text.split()
    if not parts:
        return "0"

    # 輸入格式：
    # 第 1 行: n m
    # 接著 n 行: 每行長度 m，字元為 P/H
    n = int(parts[0])
    m = int(parts[1])
    rows = parts[2:2 + n]

    # 防呆：每列最多取 m 個字元，避免異常輸入長度造成問題
    grid = [r[:m] for r in rows]
    return str(max_artillery(grid))


def main():
    """競賽入口：讀取 stdin 並輸出答案。"""
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

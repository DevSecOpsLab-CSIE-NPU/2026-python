"""題目 10093（easy 版，附詳細註解）。

重點：
1. 每一列用 bitmask 表示放炮兵的位置。
2. 先列出「單列合法」狀態：同列不能左右相距 1 或 2。
3. 做列 DP，轉移時檢查：
   - 當前列是否只放在 P
   - 當前列是否和前一列同欄衝突（距離 1）
   - 當前列是否和前二列同欄衝突（距離 2）
"""

from __future__ import annotations

import sys


def solve(grid: list[str]) -> int:
    """以列 DP 計算最大炮兵數。"""
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    # 把每一列的 P 位置做成 bitmask，1 代表可放，0 代表 H。
    row_ok = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        row_ok.append(mask)

    # 單列可用狀態：同列距離 1 和 2 都不能同時放。
    # 這裡不先看地形，只先處理「同列互攻」限制。
    states = []
    for s in range(1 << m):
        if s & (s << 1):
            continue
        if s & (s << 2):
            continue
        states.append(s)

    soldiers = {s: bin(s).count("1") for s in states}

    # dp[(prev, prev2)] = 掃描到目前列後最多放幾支。
    # prev 表示上一列狀態，prev2 表示上上列狀態。
    dp: dict[tuple[int, int], int] = {(0, 0): 0}

    for r in range(n):
        ndp: dict[tuple[int, int], int] = {}
        for (prev, prev2), best in dp.items():
            for cur in states:
                # cur 必須是 row_ok[r] 的子集合（不能放在 H）。
                if (cur & row_ok[r]) != cur:
                    continue
                # 垂直距離 1 衝突。
                if cur & prev:
                    continue
                # 垂直距離 2 衝突。
                if cur & prev2:
                    continue

                key = (cur, prev)
                # 新增當前列人數，嘗試更新最佳值。
                cand = best + soldiers[cur]
                if cand > ndp.get(key, -1):
                    ndp[key] = cand
        dp = ndp

    return max(dp.values(), default=0)


def main() -> None:
    # 輸入格式：N M + N 行地圖。
    lines = sys.stdin.buffer.read().decode().splitlines()
    if not lines:
        return

    n, _m = map(int, lines[0].split())
    grid = [lines[i + 1].strip() for i in range(n)]
    print(solve(grid))


if __name__ == "__main__":
    main()

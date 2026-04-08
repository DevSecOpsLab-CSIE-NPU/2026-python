"""題目 10093 解法（位元 DP，O(N * S^3) 的壓縮版本）。

地圖 N x M（M<=10），H 不能放，P 可放。
炮兵互相攻擊規則：
- 同一列左右距離 1 或 2 不可同時放
- 同一欄上下距離 1 或 2 不可同時放

DP 狀態設計：
- 用 bitmask 表示每一列的擺放
- 狀態 mask 需滿足同列不衝突：
  mask & (mask<<1)==0 且 mask & (mask<<2)==0
- 轉移需要看前兩列（因為縱向距離 2 也衝突）
"""

from __future__ import annotations

import sys


def popcount(x: int) -> int:
    # Python 3.9 相容寫法。
    return bin(x).count("1")


def build_row_mask(row: str) -> int:
    # 把可放置位置 P 編成 bitmask，方便後續用位元判斷。
    m = 0
    for i, ch in enumerate(row):
        if ch == "P":
            m |= 1 << i
    return m


def max_artillery(grid: list[str]) -> int:
    """回傳地圖上最多可部署的炮兵數。"""
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    # land[r] 的 1 bit 代表第 r 列該欄是 P（可放）。
    land = [build_row_mask(row) for row in grid]

    valid_states = []
    for mask in range(1 << m):
        # 同一列左右距離 1 不可同時放。
        if (mask & (mask << 1)) != 0:
            continue
        # 同一列左右距離 2 不可同時放。
        if (mask & (mask << 2)) != 0:
            continue
        valid_states.append(mask)

    cnt = {s: popcount(s) for s in valid_states}

    # dp[(prev, prev2)] = 目前處理到某列後的最佳值
    dp: dict[tuple[int, int], int] = {(0, 0): 0}

    for r in range(n):
        ndp: dict[tuple[int, int], int] = {}
        for (prev, prev2), cur_best in dp.items():
            for cur in valid_states:
                # 只能放在平原 P（cur 必須是 land[r] 的子集合）。
                if (cur & land[r]) != cur:
                    continue
                # 與前一列同欄衝突（上下距離 1）。
                if (cur & prev) != 0:
                    continue
                # 與前二列同欄衝突（上下距離 2）。
                if (cur & prev2) != 0:
                    continue

                key = (cur, prev)
                val = cur_best + cnt[cur]
                old = ndp.get(key)
                if old is None or val > old:
                    ndp[key] = val
        dp = ndp

    return max(dp.values(), default=0)


def main() -> None:
    # 輸入：N M + N 行地圖字串。
    lines = sys.stdin.buffer.read().decode().splitlines()
    if not lines:
        return

    n, m = map(int, lines[0].split())
    grid = [lines[i + 1].strip() for i in range(n)]
    print(max_artillery(grid))


if __name__ == "__main__":
    main()

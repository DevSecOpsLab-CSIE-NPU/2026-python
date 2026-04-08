"""UVA 10093 正式版。

這題是狀態壓縮 DP：
每一列用 bitmask 表示炮兵位置，
再記錄前兩列的狀態，避免垂直方向互相攻擊。
"""

from __future__ import annotations

import sys


def valid_masks(width: int, terrain_mask: int):
    """列出某一列所有可用的炮兵擺法。"""

    result = []
    limit = 1 << width
    for mask in range(limit):
        # 只能放在平原上。
        if mask & ~terrain_mask:
            continue
        # 同一列內，不能在距離 1 或 2 的位置同時放炮兵。
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        result.append(mask)
    return result


def solve(text: str) -> str:
    parts = text.split()
    if not parts:
        return ""

    rows = int(parts[0])
    cols = int(parts[1])
    grid = parts[2 : 2 + rows]

    row_masks = []
    all_open = (1 << cols) - 1
    for row in grid:
        blocked = 0
        for index, cell in enumerate(row):
            if cell == "H":
                blocked |= 1 << index
        row_masks.append(valid_masks(cols, all_open ^ blocked))

    # dp[(上一列, 上上列)] = 目前最多能放幾支
    dp = {(0, 0): 0}
    for masks in row_masks:
        next_dp = {}
        for (prev1, prev2), current_best in dp.items():
            for cur in masks:
                # 同欄位若相隔 1 或 2 列都會互相攻擊。
                if cur & prev1:
                    continue
                if cur & prev2:
                    continue
                key = (cur, prev1)
                score = current_best + cur.bit_count()
                if score > next_dp.get(key, -1):
                    next_dp[key] = score
        dp = next_dp

    return str(max(dp.values(), default=0))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
"""10093 的好記憶版本。

做法就是：
每一列先列出所有合法擺法，
再用 DP 記住前兩列的配置。
"""

from __future__ import annotations

import sys


def build_masks(width: int, open_cells: int):
    masks = []
    for mask in range(1 << width):
        if mask & ~open_cells:
            continue
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        masks.append(mask)
    return masks


def solve(text: str) -> str:
    tokens = text.split()
    if not tokens:
        return ""

    n = int(tokens[0])
    m = int(tokens[1])
    board = tokens[2 : 2 + n]

    all_open = (1 << m) - 1
    rows = []
    for row in board:
        blocked = 0
        for col, ch in enumerate(row):
            if ch == "H":
                blocked |= 1 << col
        rows.append(build_masks(m, all_open ^ blocked))

    dp = {(0, 0): 0}
    for row_masks in rows:
        new_dp = {}
        for (prev_row, prev_prev_row), best in dp.items():
            for mask in row_masks:
                if mask & prev_row:
                    continue
                if mask & prev_prev_row:
                    continue
                next_state = (mask, prev_row)
                new_score = best + mask.bit_count()
                if new_score > new_dp.get(next_state, -1):
                    new_dp[next_state] = new_score
        dp = new_dp

    return str(max(dp.values(), default=0))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
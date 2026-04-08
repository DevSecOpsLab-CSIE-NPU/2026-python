"""10093 手打版。

這題的關鍵不是找單一列的最佳擺法，
而是要把前兩列也一起記住，
這樣才不會漏掉垂直方向兩格內的攻擊限制。
"""

from __future__ import annotations

import sys


def row_states(width: int, open_mask: int):
    result = []
    for state in range(1 << width):
        if state & ~open_mask:
            continue
        if state & (state << 1):
            continue
        if state & (state << 2):
            continue
        result.append(state)
    return result


def solve(text: str) -> str:
    data = text.split()
    if not data:
        return ""

    n = int(data[0])
    m = int(data[1])
    grid = data[2 : 2 + n]

    all_open = (1 << m) - 1
    states_per_row = []
    for row in grid:
        blocked = 0
        for col, ch in enumerate(row):
            if ch == "H":
                blocked |= 1 << col
        states_per_row.append(row_states(m, all_open ^ blocked))

    dp = {(0, 0): 0}
    for states in states_per_row:
        next_dp = {}
        for (prev, prev_prev), best in dp.items():
            for cur in states:
                if cur & prev:
                    continue
                if cur & prev_prev:
                    continue
                new_state = (cur, prev)
                score = best + cur.bit_count()
                if score > next_dp.get(new_state, -1):
                    next_dp[new_state] = score
        dp = next_dp

    return str(max(dp.values(), default=0))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
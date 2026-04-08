from __future__ import annotations

import sys


def get_valid_states(m: int) -> list[int]:
    """產生一列中可擺放炮兵的所有合法 bitmask。

    規則：同一列內，任兩門炮的水平距離不能是 1 或 2。
    """
    result = []
    for state in range(1 << m):
        if (state & (state << 1)) != 0:
            continue
        if (state & (state << 2)) != 0:
            continue
        result.append(state)
    return result


def solve(data: str) -> str:
    items = data.split()
    if not items:
        return ""

    n = int(items[0])
    m = int(items[1])
    grid = items[2 : 2 + n]

    # 把每一列的平原位置轉成 bitmask（P=1, H=0）。
    plains = []
    for row in grid:
        mask = 0
        for col, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << col
        plains.append(mask)

    all_states = get_valid_states(m)

    # 每列可用狀態：要同時符合「狀態合法」與「不落在山地」。
    row_states: list[list[int]] = []
    for r in range(n):
        candidates = []
        for state in all_states:
            if (state & ~plains[r]) == 0:
                candidates.append(state)
        row_states.append(candidates)

    # DP 鍵值 (上一列狀態, 上上列狀態) -> 目前最大炮兵數。
    # 需要記兩列，因為垂直攻擊距離到 2。
    dp = {(0, 0): 0}

    for r in range(n):
        next_dp: dict[tuple[int, int], int] = {}
        for cur in row_states[r]:
            cur_count = cur.bit_count()
            for (prev, prev2), best in dp.items():
                # 垂直方向：不能和上一列、上上列同欄衝突。
                if (cur & prev) != 0:
                    continue
                if (cur & prev2) != 0:
                    continue

                key = (cur, prev)
                value = best + cur_count
                old = next_dp.get(key)
                if old is None or value > old:
                    next_dp[key] = value
        dp = next_dp

    return str(max(dp.values(), default=0))


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()

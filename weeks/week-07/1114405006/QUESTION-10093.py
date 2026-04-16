"""
UVA/ZeroJudge 10093（炮兵陣地）
在 N x M 地圖上放置最多炮兵，限制：
1) 只能放在平原 P
2) 同一列中，左右距離 1 或 2 不可同時放（橫向攻擊）
3) 同一欄中，上下距離 1 或 2 不可同時放（縱向攻擊）
"""

from __future__ import annotations

import sys


def generate_valid_states(m: int) -> list[int]:
    """產生所有單列可行狀態（不含左右 1、2 格衝突）。"""
    states = []
    for s in range(1 << m):
        if (s & (s << 1)) != 0:
            continue
        if (s & (s << 2)) != 0:
            continue
        states.append(s)
    return states


def count_bits(x: int) -> int:
    return x.bit_count()


def max_artillery(n: int, m: int, grid: list[str]) -> int:
    # row_mask[i]：第 i 列可放位置（P=1, H=0）
    row_mask = []
    for r in range(n):
        mask = 0
        for c, ch in enumerate(grid[r]):
            if ch == "P":
                mask |= 1 << c
        row_mask.append(mask)

    states = generate_valid_states(m)
    state_count = len(states)
    bits = [count_bits(s) for s in states]

    # dp_prev2[p2][p1] 代表處理到上一列時：
    # - 前前列狀態索引 = p2
    # - 前一列狀態索引 = p1
    # 的最大炮兵數。
    neg_inf = -10**9
    dp_prev2 = [[neg_inf] * state_count for _ in range(state_count)]

    # 初始：尚未放任何列，視為兩列都是 0 狀態。
    zero_idx = states.index(0)
    dp_prev2[zero_idx][zero_idx] = 0

    for r in range(n):
        dp_cur = [[neg_inf] * state_count for _ in range(state_count)]
        for p2 in range(state_count):
            for p1 in range(state_count):
                base = dp_prev2[p2][p1]
                if base == neg_inf:
                    continue

                s2 = states[p2]
                s1 = states[p1]

                # 嘗試本列狀態 sc
                for pc in range(state_count):
                    sc = states[pc]

                    # 只能放在本列平原上
                    if (sc & ~row_mask[r]) != 0:
                        continue

                    # 與前一列、前前列同欄不可重疊（縱向 1、2 格衝突）
                    if (sc & s1) != 0:
                        continue
                    if (sc & s2) != 0:
                        continue

                    new_val = base + bits[pc]
                    if new_val > dp_cur[p1][pc]:
                        dp_cur[p1][pc] = new_val

        dp_prev2 = dp_cur

    ans = 0
    for row in dp_prev2:
        best = max(row)
        if best > ans:
            ans = best
    return ans


def solve(text: str) -> str:
    tokens = text.strip().split()
    if not tokens:
        return ""

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))
    grid = [next(it) for _ in range(n)]

    return str(max_artillery(n, m, grid))


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()

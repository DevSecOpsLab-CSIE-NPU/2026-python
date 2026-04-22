from __future__ import annotations

from collections import defaultdict
import sys


MOD = 1_000_000_007


def count_placements(grid: list[list[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    # state 的 bit c 表示「(r-1,c) 到 (r,c) 這條垂直邊是否已被選」
    # state 的 bit m 表示「(r,c-1) 到 (r,c) 這條水平邊是否已被選」
    dp: dict[int, int] = {0: 1}

    for r in range(n):
        for c in range(m):
            nxt: defaultdict[int, int] = defaultdict(int)

            for state, ways in dp.items():
                up = (state >> c) & 1
                left = (state >> m) & 1
                blocked = grid[r][c] == 0

                if blocked:
                    if up or left:
                        continue
                    new_state = state & ~(1 << m)
                    nxt[new_state] = (nxt[new_state] + ways) % MOD
                    continue

                right_ok = c + 1 < m and grid[r][c + 1] == 1
                down_ok = r + 1 < n and grid[r + 1][c] == 1

                for right in (0, 1):
                    if right and not right_ok:
                        continue
                    for down in (0, 1):
                        if down and not down_ok:
                            continue

                        if up + left + right + down != 2:
                            continue

                        new_state = state
                        new_state &= ~(1 << m)
                        new_state &= ~(1 << c)
                        if right:
                            new_state |= 1 << m
                        if down:
                            new_state |= 1 << c

                        nxt[new_state] = (nxt[new_state] + ways) % MOD

            dp = nxt

        # 每列結束時，不允許還有往右的懸空邊
        dp = {s: v for s, v in dp.items() if ((s >> m) & 1) == 0}

    return dp.get(0, 0)


def solve(data: str) -> str:
    tokens = data.split()
    i = 0
    t = int(tokens[i])
    i += 1

    outputs: list[str] = []
    for case_idx in range(1, t + 1):
        n = int(tokens[i])
        m = int(tokens[i + 1])
        i += 2

        grid = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                grid[r][c] = int(tokens[i])
                i += 1

        ans = count_placements(grid)
        outputs.append(f"Case {case_idx}: {ans}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

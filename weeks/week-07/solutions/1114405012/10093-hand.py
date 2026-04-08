"""10093 easy-hand：手打版（位元 DP）。"""

import sys


def solve(grid):
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    # row_ok[r]：第 r 列可放置位置（P）的 bitmask。
    row_ok = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == 'P':
                mask |= 1 << c
        row_ok.append(mask)

    # 列舉同列合法狀態：距離 1、2 都不能同時放。
    states = []
    for s in range(1 << m):
        if s & (s << 1):
            continue
        if s & (s << 2):
            continue
        states.append(s)

    soldiers = {s: bin(s).count('1') for s in states}

    # dp[(prev, prev2)] = 掃描到目前列的最大炮兵數。
    dp = {(0, 0): 0}

    for r in range(n):
        ndp = {}
        for (prev, prev2), best in dp.items():
            for cur in states:
                if (cur & row_ok[r]) != cur:
                    continue
                if cur & prev:
                    continue
                if cur & prev2:
                    continue

                key = (cur, prev)
                cand = best + soldiers[cur]
                if cand > ndp.get(key, -1):
                    ndp[key] = cand
        dp = ndp

    return max(dp.values(), default=0)


def main():
    lines = sys.stdin.buffer.read().decode().splitlines()
    if not lines:
        return

    n, _m = map(int, lines[0].split())
    grid = [lines[i + 1].strip() for i in range(n)]
    print(solve(grid))


if __name__ == '__main__':
    main()

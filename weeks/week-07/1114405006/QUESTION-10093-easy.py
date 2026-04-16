"""
QUESTION-10093-easy
教學版狀壓 DP：重點是「每列是一個 bitmask」，並記住只需要看前三列關係。
"""

from __future__ import annotations

import sys


def build_states(m: int) -> list[int]:
    """建立所有「單列內不互打」的放置狀態。"""
    res = []
    for s in range(1 << m):
        # 同列左右相差 1 或 2 格都不能同時放炮兵
        if s & (s << 1):
            continue
        if s & (s << 2):
            continue
        res.append(s)
    return res


def solve(inp: str) -> str:
    data = inp.strip().split()
    if not data:
        return ""

    n = int(data[0])
    m = int(data[1])
    g = data[2 : 2 + n]

    # 把每一列可放位置轉成 bitmask：P=1、H=0
    land = []
    for r in range(n):
        mask = 0
        for c, ch in enumerate(g[r]):
            if ch == "P":
                mask |= 1 << c
        land.append(mask)

    states = build_states(m)
    s_len = len(states)
    cnt = [s.bit_count() for s in states]
    neg = -10**9

    # dp[a][b]：目前掃到某列前，
    # 前前列狀態索引 a、前一列狀態索引 b 的最佳值
    dp = [[neg] * s_len for _ in range(s_len)]
    z = states.index(0)
    dp[z][z] = 0

    for r in range(n):
        ndp = [[neg] * s_len for _ in range(s_len)]

        for a in range(s_len):
            for b in range(s_len):
                cur_best = dp[a][b]
                if cur_best == neg:
                    continue

                sa = states[a]  # 前前列
                sb = states[b]  # 前一列

                for c_idx in range(s_len):
                    sc = states[c_idx]  # 本列

                    # 本列必須都在平原上
                    if sc & ~land[r]:
                        continue
                    # 與上 1 列、上 2 列同欄不能重疊
                    if sc & sb:
                        continue
                    if sc & sa:
                        continue

                    val = cur_best + cnt[c_idx]
                    if val > ndp[b][c_idx]:
                        ndp[b][c_idx] = val

        dp = ndp

    ans = 0
    for row in dp:
        row_max = max(row)
        if row_max > ans:
            ans = row_max

    return str(ans)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()

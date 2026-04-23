"""UVA/ZeroJudge 10093（炮兵部署）解答。

N<=100, M<=10。
使用狀態壓縮 DP（逐列處理、記住前兩列）。
"""

from __future__ import annotations

import sys


NEG = -10**18


def bit_count(x: int) -> int:
    return bin(x).count("1")


def solve(input_data: str) -> str:
    parts = input_data.split()
    if not parts:
        return ""

    it = iter(parts)
    n = int(next(it))
    m = int(next(it))

    rows = [next(it).strip() for _ in range(n)]

    # 把每列可放置（P）的格子做成 bitmask
    plains = []
    for r in rows:
        mask = 0
        for j, ch in enumerate(r):
            if ch == "P":
                mask |= 1 << j
        plains.append(mask)

    # 列內合法狀態：同列不能相鄰，也不能隔一格（距離 2）
    states = []
    for mask in range(1 << m):
        if (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0:
            states.append(mask)

    state_count = len(states)
    pop = [bit_count(s) for s in states]

    # 預先計算每列可用狀態（不能放在 H）
    valid_states_per_row = []
    for i in range(n):
        valid = []
        p = plains[i]
        for si, st in enumerate(states):
            if (st & ~p) == 0:
                valid.append(si)
        valid_states_per_row.append(valid)

    # dp_prev[p1][p2]：已處理到前一列時，
    # 前一列狀態索引為 p1，前二列狀態索引為 p2 的最大值
    dp_prev = {(0, 0): 0}

    for i in range(n):
        dp_cur = {}
        valid_cur = valid_states_per_row[i]

        for (p1, p2), best in dp_prev.items():
            st1 = states[p1]
            st2 = states[p2]
            for c in valid_cur:
                stc = states[c]

                # 縱向攻擊距離 1 與 2 都不允許同欄位
                if (stc & st1) != 0:
                    continue
                if (stc & st2) != 0:
                    continue

                key = (c, p1)
                cand = best + pop[c]
                old = dp_cur.get(key, NEG)
                if cand > old:
                    dp_cur[key] = cand

        dp_prev = dp_cur

    ans = max(dp_prev.values()) if dp_prev else 0
    return str(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()

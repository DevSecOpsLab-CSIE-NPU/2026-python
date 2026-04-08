from __future__ import annotations

import sys


def build_states(m: int) -> list[int]:
    states = []
    for s in range(1 << m):
        if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
            states.append(s)
    return states


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    n = int(parts[0])
    m = int(parts[1])
    rows = parts[2 : 2 + n]

    plains = []
    for r in rows:
        mask = 0
        for j, ch in enumerate(r):
            if ch == "P":
                mask |= 1 << j
        plains.append(mask)

    states = build_states(m)
    row_states = []
    for i in range(n):
        row_states.append([s for s in states if (s & ~plains[i]) == 0])

    dp = {(0, 0): 0}
    for i in range(n):
        nxt = {}
        for cur in row_states[i]:
            cnt = cur.bit_count()
            for (prev, prev2), best in dp.items():
                if (cur & prev) or (cur & prev2):
                    continue
                key = (cur, prev)
                val = best + cnt
                if key not in nxt or val > nxt[key]:
                    nxt[key] = val
        dp = nxt

    return str(max(dp.values(), default=0))


if __name__ == "__main__":
    out = solve(sys.stdin.read())
    if out:
        sys.stdout.write(out)

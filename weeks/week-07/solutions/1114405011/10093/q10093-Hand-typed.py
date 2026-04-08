from __future__ import annotations
import sys
from collections import defaultdict


def states(m: int) -> list[int]:
    r = []
    for s in range(1 << m):
        if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
            r.append(s)
    return r


def solve_core(board: list[str]) -> int:
    n = len(board)
    m = len(board[0])
    tm = []
    for row in board:
        x = 0
        for j, ch in enumerate(row):
            if ch == "P":
                x |= 1 << j
        tm.append(x)
    st = states(m)
    pc = {s: s.bit_count() for s in st}
    valid = []
    for i in range(n):
        valid.append([s for s in st if (s & ~tm[i]) == 0])
    dp = {(0, 0): 0}
    for r in range(n):
        ndp = defaultdict(lambda: -1)
        for (a, b), v in dp.items():
            for c in valid[r]:
                if (c & b) != 0:
                    continue
                if (c & a) != 0:
                    continue
                nv = v + pc[c]
                k = (b, c)
                if nv > ndp[k]:
                    ndp[k] = nv
        dp = ndp
    return max(dp.values(), default=0)


def solve(data: str) -> str:
    t = data.strip().split()
    if not t:
        return ""
    n = int(t[0])
    m = int(t[1])
    rows = t[2 : 2 + n]
    if any(len(r) != m for r in rows):
        return ""
    return str(solve_core(rows))


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))

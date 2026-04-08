from __future__ import annotations

import sys


def valid_row_states(m: int) -> list[int]:
    states = []
    for s in range(1 << m):
        if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
            states.append(s)
    return states


def popcount(x: int) -> int:
    return x.bit_count()


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    it = iter(parts)
    n = int(next(it))
    m = int(next(it))
    rows = [next(it).strip() for _ in range(n)]

    plains_mask = []
    for r in rows:
        mask = 0
        for j, ch in enumerate(r):
            if ch == "P":
                mask |= 1 << j
        plains_mask.append(mask)

    states = valid_row_states(m)
    row_candidates = []
    for i in range(n):
        cand = [s for s in states if (s & ~plains_mask[i]) == 0]
        row_candidates.append(cand)

    dp_prev = {(0, 0): 0}
    for r in range(n):
        dp_cur = {}
        for cur in row_candidates[r]:
            cur_cnt = popcount(cur)
            for (prev, prev2), best in dp_prev.items():
                if (cur & prev) != 0:
                    continue
                if (cur & prev2) != 0:
                    continue
                key = (cur, prev)
                val = best + cur_cnt
                if key not in dp_cur or val > dp_cur[key]:
                    dp_cur[key] = val
        dp_prev = dp_cur

    return str(max(dp_prev.values(), default=0))


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()

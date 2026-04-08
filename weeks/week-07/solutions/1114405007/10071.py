from __future__ import annotations

import sys
from collections import defaultdict


def solve(data: str) -> str:
    vals = [int(x) for x in data.split()]
    if not vals:
        return ""

    n = vals[0]
    arr = vals[1 : 1 + n]

    pair_count: dict[int, int] = defaultdict(int)
    for a in arr:
        for b in arr:
            pair_count[a + b] += 1

    triple_count: dict[int, int] = defaultdict(int)
    for ps, cnt in pair_count.items():
        for c in arr:
            triple_count[ps + c] += cnt

    ans = 0
    for f in arr:
        target = f
        total = 0
        for ps, cnt in pair_count.items():
            total += cnt * triple_count.get(target - ps, 0)
        ans += total

    return str(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()

from __future__ import annotations

import sys


def day_group_size(s: int, d: int) -> int:
    lo, hi = 0, 2_000_000_000
    while lo < hi:
        mid = (lo + hi) // 2
        days = (mid + 1) * (2 * s + mid) // 2
        if days >= d:
            hi = mid
        else:
            lo = mid + 1
    return s + lo


def solve(data: str) -> str:
    vals = [int(x) for x in data.split()]
    out = []
    for i in range(0, len(vals), 2):
        s = vals[i]
        d = vals[i + 1]
        out.append(str(day_group_size(s, d)))
    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()

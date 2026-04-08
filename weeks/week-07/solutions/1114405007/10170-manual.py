from __future__ import annotations

import sys


def solve_one(s: int, d: int) -> int:
    # 手打版：二分找最小 k，使 (k+1)(2s+k)/2 >= d。
    lo, hi = 0, 2_000_000_000
    while lo < hi:
        mid = (lo + hi) // 2
        total_days = (mid + 1) * (2 * s + mid) // 2
        if total_days >= d:
            hi = mid
        else:
            lo = mid + 1
    return s + lo


def solve(data: str) -> str:
    vals = [int(x) for x in data.split()]
    ans = []
    for i in range(0, len(vals), 2):
        ans.append(str(solve_one(vals[i], vals[i + 1])))
    return "\n".join(ans)


if __name__ == "__main__":
    out = solve(sys.stdin.read())
    if out:
        sys.stdout.write(out)

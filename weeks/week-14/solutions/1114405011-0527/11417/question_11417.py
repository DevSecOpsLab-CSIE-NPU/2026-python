"""UVA 11417 - GCD（一般版，繁中註解）"""

from __future__ import annotations

import math
import sys


def build_table(limit: int = 500) -> list[int]:
    """預先計算每個 N 的答案，讓查詢 O(1)。"""
    pair_sum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i + 1, limit + 1):
            pair_sum[j] += math.gcd(i, j)

    ans = [0] * (limit + 1)
    for n in range(2, limit + 1):
        ans[n] = ans[n - 1] + pair_sum[n]
    return ans


def solve(data: str) -> str:
    values = [int(x) for x in data.strip().split() if x.strip()]
    if not values:
        return ""

    table = build_table(500)
    out: list[str] = []
    for n in values:
        if n == 0:
            break
        out.append(str(table[n]))
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

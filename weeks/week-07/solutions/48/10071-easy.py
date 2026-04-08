"""10071 的好記憶版本。

核心做法：
1. 先算出所有三數和的次數。
2. 再算所有兩數和的次數。
3. 用 f - (d + e) 去查三數和表。
"""

from __future__ import annotations

import sys
from collections import defaultdict


def solve(text: str) -> str:
    data = list(map(int, text.split()))
    if not data:
        return ""

    n = data[0]
    nums = data[1 : n + 1]

    three_count = defaultdict(int)
    for x in nums:
        for y in nums:
            xy = x + y
            for z in nums:
                three_count[xy + z] += 1

    two_count = defaultdict(int)
    for p in nums:
        for q in nums:
            two_count[p + q] += 1

    ans = 0
    for f in nums:
        for pair_sum, pair_times in two_count.items():
            ans += pair_times * three_count.get(f - pair_sum, 0)

    return str(ans)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
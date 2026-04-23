"""UVA/ZeroJudge 10071 簡單版（easy）。

這版偏向易懂：
- 用 dict 統計三元和與二元和出現次數
- 最後對每個 f 做卷積式累加

概念直觀，仍可在 N<=100 內運作。
"""

from __future__ import annotations

import sys
from collections import defaultdict


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    if not nums:
        return ""

    n = nums[0]
    s = nums[1 : 1 + n]

    cnt2 = defaultdict(int)
    for d in s:
        for e in s:
            cnt2[d + e] += 1

    cnt3 = defaultdict(int)
    for a in s:
        for b in s:
            for c in s:
                cnt3[a + b + c] += 1

    ans = 0
    for f in s:
        for t, c3 in cnt3.items():
            ans += c3 * cnt2.get(f - t, 0)

    return str(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()

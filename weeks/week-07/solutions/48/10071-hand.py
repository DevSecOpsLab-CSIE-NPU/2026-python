"""10071 手打版。

這版寫法故意拆得比較直白：
先記錄三個數字的和，再用兩個數字的和去反查，
就能把六元組的數量算出來。
"""

from __future__ import annotations

import sys
from collections import defaultdict


def solve(text: str) -> str:
    values = list(map(int, text.split()))
    if not values:
        return ""

    n = values[0]
    arr = values[1 : n + 1]

    # 三個數字的總和 -> 出現次數
    sum3 = defaultdict(int)
    for a in arr:
        for b in arr:
            ab = a + b
            for c in arr:
                sum3[ab + c] += 1

    # 兩個數字的總和 -> 出現次數
    sum2 = defaultdict(int)
    for d in arr:
        for e in arr:
            sum2[d + e] += 1

    # a + b + c + d + e = f
    # => a + b + c = f - d - e
    answer = 0
    for f in arr:
        for se, cnt in sum2.items():
            answer += cnt * sum3.get(f - se, 0)

    return str(answer)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
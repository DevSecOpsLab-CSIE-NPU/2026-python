"""10170 手打版。

這題可以直接看成等差級數：
S 人住 S 天、S+1 人住 S+1 天，
因此第 D 天落在哪一團，只要找累積天數第一次超過 D 的位置。
"""

from __future__ import annotations

import math
import sys


def find_people(start: int, day: int) -> int:
    # x 代表從起始團體開始，已經經過幾個團體。
    # 累積天數公式：x * (2 * start + x - 1) / 2
    base = 2 * start - 1
    root = math.isqrt(base * base + 8 * day)
    x = (root - base) // 2
    if x < 1:
        x = 1
    while x * (x + base) < 2 * day:
        x += 1
    return start + x - 1


def solve(text: str) -> str:
    data = list(map(int, text.split()))
    if not data:
        return ""

    result = []
    for i in range(0, len(data), 2):
        result.append(str(find_people(data[i], data[i + 1])))
    return "\n".join(result)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
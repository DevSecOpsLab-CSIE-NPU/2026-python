"""UVA 10170 正式版。

第 D 天住的人數，等於找到第一個讓累積天數 >= D 的團體大小。
"""

from __future__ import annotations

import math
import sys


def group_size(start: int, day: int) -> int:
    """找出第 day 天對應的團體人數。"""

    # 令 x = 從起始團體算起，已經出現的團體數量。
    # 累積天數 = x * (2 * start + x - 1) / 2
    # 需要最小的 x 使得它 >= day。
    base = 2 * start - 1
    discriminant = base * base + 8 * day
    root = math.isqrt(discriminant)

    x = max(1, (root - base) // 2)
    while x * (x + base) < 2 * day:
        x += 1

    return start + x - 1


def solve(text: str) -> str:
    numbers = list(map(int, text.split()))
    if not numbers:
        return ""

    output = []
    for index in range(0, len(numbers), 2):
        start = numbers[index]
        day = numbers[index + 1]
        output.append(str(group_size(start, day)))
    return "\n".join(output)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
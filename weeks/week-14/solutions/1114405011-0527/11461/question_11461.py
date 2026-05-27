"""UVA 11461 - Square Numbers（一般版，繁中註解）"""

from __future__ import annotations

import math
import sys


def count_squares(a: int, b: int) -> int:
    """計算 [a, b] 區間內的完全平方數個數。"""
    return math.isqrt(b) - math.isqrt(a - 1)


def solve(data: str) -> str:
    nums = [int(x) for x in data.strip().split() if x.strip()]
    out: list[str] = []

    for i in range(0, len(nums), 2):
        a = nums[i]
        b = nums[i + 1]
        if a == 0 and b == 0:
            break
        out.append(str(count_squares(a, b)))

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

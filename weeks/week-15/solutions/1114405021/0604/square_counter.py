"""平方數計數實作

提供 `count_squares(a, b) -> int`：回傳區間 [a, b] 之間完全平方數的個數。
若 a > b，丟出 ValueError("a must be <= b")。
"""

import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    # 計算最小的 k 使 k^2 >= a，以及最大的 k 使 k^2 <= b
    lower = math.isqrt(a)
    if lower * lower < a:
        lower += 1

    upper = math.isqrt(b)

    return max(0, upper - lower + 1)

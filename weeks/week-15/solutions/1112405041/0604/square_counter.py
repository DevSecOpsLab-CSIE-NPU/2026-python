"""平方數計數實作
"""

import math


def count_squares(a: int, b: int) -> int:
    """回傳 [a, b] 區間內完全平方數的個數。"""
    if a > b:
        raise ValueError("a must be <= b")

    # 找出第一個大於等於 a 的整數根
    start = math.ceil(math.sqrt(a))
    # 找出最後一個小於等於 b 的整數根
    end = math.floor(math.sqrt(b))

    if start > end:
        return 0
    return end - start + 1

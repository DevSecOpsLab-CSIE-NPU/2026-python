"""平方數計數。"""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    return isqrt(b) - isqrt(a - 1)

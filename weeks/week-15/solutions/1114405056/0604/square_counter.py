import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")
    return math.isqrt(b) - math.isqrt(a - 1)

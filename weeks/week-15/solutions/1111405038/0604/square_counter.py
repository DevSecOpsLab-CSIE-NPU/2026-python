import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    start = math.isqrt(a - 1) + 1
    end = math.isqrt(b)

    if start > end:
        return 0

    return end - start + 1
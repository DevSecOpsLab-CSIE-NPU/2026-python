import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")
    # isqrt(b) - isqrt(a-1) 直接算出 [a,b] 內完全平方數個數
    return math.isqrt(b) - math.isqrt(a - 1)

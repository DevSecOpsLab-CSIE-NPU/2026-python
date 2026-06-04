from math import isqrt


def count_squares(a: int, b: int) -> int:
    """Count perfect squares in the inclusive range [a, b]."""
    if a > b:
        raise ValueError("a must be <= b")

    if b < 0:
        return 0

    start = max(a, 0)
    low = isqrt(start - 1) + 1 if start > 0 else 0
    high = isqrt(b)

    if low > high:
        return 0

    return high - low + 1

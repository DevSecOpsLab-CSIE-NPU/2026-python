"""Count perfect squares within an inclusive range."""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    lower = isqrt(a)
    if lower * lower < a:
        lower += 1

    upper = isqrt(b)
    return max(0, upper - lower + 1)

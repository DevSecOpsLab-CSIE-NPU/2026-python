"""Count perfect squares in an inclusive integer range."""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    lower_root = isqrt(a - 1)
    upper_root = isqrt(b)
    return upper_root - lower_root
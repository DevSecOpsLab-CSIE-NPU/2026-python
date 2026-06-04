"""Count perfect squares in an inclusive integer range."""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    """Return number of perfect squares in [a, b]."""
    if a > b:
        raise ValueError("a must be <= b")

    left = isqrt(a - 1) + 1
    right = isqrt(b)
    if left > right:
        return 0
    return right - left + 1

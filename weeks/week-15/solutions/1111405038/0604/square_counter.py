"""Count perfect squares in an inclusive range."""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    """Return how many perfect squares are in [a, b]."""
    if a > b:
        raise ValueError("a must be <= b")

    left = isqrt(a - 1)
    right = isqrt(b)
    return right - left

"""Count perfect squares in an inclusive range."""

from math import isqrt


def count_squares(a: int, b: int) -> int:
    """Return how many perfect squares are in the inclusive range [a, b]."""
    if a > b:
        raise ValueError("a must be <= b")

    start = isqrt(a)
    if start * start < a:
        start += 1

    end = isqrt(b)
    if start > end:
        return 0

    return end - start + 1

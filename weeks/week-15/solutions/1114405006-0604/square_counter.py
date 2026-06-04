"""Count squares solution for TDD practice.

Provides `count_squares(a, b)` which returns the number of perfect
square integers in the inclusive range [a, b]. Raises ValueError if a > b.
"""
import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")
    if b < 0:
        return 0
    # find smallest integer s such that s*s >= a
    s = math.isqrt(max(a, 0))
    if s * s < a:
        s += 1
    e = math.isqrt(b)
    if s > e:
        return 0
    return e - s + 1

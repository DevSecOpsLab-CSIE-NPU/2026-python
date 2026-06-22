"""Digit root in a fixed base.

This submission uses base 8.
"""

BASE = 8


def _sum_digits_in_base(n: int, base: int) -> int:
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total


def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= BASE:
        n = _sum_digits_in_base(n, BASE)
    return n
from math import isqrt


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    first_root = 0 if a <= 0 else isqrt(a - 1) + 1
    last_root = isqrt(b)

    return max(0, last_root - first_root + 1)

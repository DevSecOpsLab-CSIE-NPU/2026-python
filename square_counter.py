import math


def count_squares(a: int, b: int) -> int:
    """回傳區間 [a, b] 內完全平方數的個數。

    若 a > b 則丟出 ValueError。
    """
    if a > b:
        raise ValueError("a must be <= b")

    if b < 0:
        return 0

    start_n = math.isqrt(max(a, 0))
    if start_n * start_n < max(a, 0):
        start_n += 1

    end_n = math.isqrt(b)

    if end_n < start_n:
        return 0

    return end_n - start_n + 1

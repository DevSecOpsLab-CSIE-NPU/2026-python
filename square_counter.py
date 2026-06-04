import math


def count_squares(a: int, b: int) -> int:
    """回傳區間 [a, b] 內完全平方數的個數。

    若 a > b 則丟出 ValueError。
    """
    if a > b:
        raise ValueError("a must be <= b")

    # 若 b < 0，沒有非負平方數
    if b < 0:
        return 0

    start = max(a, 0)
    start_n = math.isqrt(start)
    if start_n * start_n < start:
        start_n += 1
    end_n = math.isqrt(b)

    if end_n < start_n:
        return 0

    return end_n - start_n + 1

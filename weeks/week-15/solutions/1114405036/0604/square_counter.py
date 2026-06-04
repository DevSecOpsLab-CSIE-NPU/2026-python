import math


def count_squares(a: int, b: int) -> int:
    if a > b:
        raise ValueError("a must be <= b")

    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)

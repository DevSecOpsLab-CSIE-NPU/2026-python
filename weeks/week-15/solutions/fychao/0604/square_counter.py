import math


def count_squares(a: int, b: int) -> int:
    """Return the number of perfect squares in the inclusive interval [a, b].

    Raises ValueError if a > b.
    """
    if a > b:
        raise ValueError("a must be <= b")
    if a < 1 or b < 1:
        # follow problem statement that inputs are positive integers
        raise ValueError("a and b must be positive integers")

    lo = math.ceil(math.sqrt(a))
    hi = math.floor(math.sqrt(b))
    return max(0, hi - lo + 1)

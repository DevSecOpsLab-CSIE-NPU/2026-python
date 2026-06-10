def digit_root(n: int) -> int:
    """Return the digital root of n.

    Repeatedly sum decimal digits of n until a single digit remains.
    Raise ValueError("n must be >= 1") when n < 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    # digital root formula for n >= 1
    return 1 + (n - 1) % 9

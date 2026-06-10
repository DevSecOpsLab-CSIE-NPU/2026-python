def digit_root(n: int) -> int:
    """Return the digital root of n.

    Repeatedly sum the digits of n until a single-digit number remains.
    Raise ValueError("n must be >= 1") for n < 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= 10:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s

    return n

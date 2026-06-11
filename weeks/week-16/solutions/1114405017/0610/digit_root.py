def digit_root(n: int) -> int:
    """Return the digital root of n.

    Repeatedly sum the digits of n until a single-digit result remains.

    Raises ValueError("n must be >= 1") if n < 1.
    """
    if not isinstance(n, int):
        # Let Python raise a TypeError for non-int inputs (tests specify int inputs).
        raise TypeError("n must be an int")

    if n < 1:
        raise ValueError("n must be >= 1")

    # Use the digital root congruence formula for efficiency:
    # For n > 0, digital root = 1 + ((n - 1) % 9)
    if n < 10:
        return n
    return 1 + ((n - 1) % 9)

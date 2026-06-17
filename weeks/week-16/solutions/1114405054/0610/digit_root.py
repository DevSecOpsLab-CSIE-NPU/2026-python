def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    return 1 + (n - 1) % 9

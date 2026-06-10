def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

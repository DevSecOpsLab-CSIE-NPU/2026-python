def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    while n >= 10:
        total = 0
        while n:
            total += n % 10
            n //= 10
        n = total
    return n

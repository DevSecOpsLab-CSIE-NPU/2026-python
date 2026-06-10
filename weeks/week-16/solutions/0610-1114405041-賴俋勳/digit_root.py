def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= 10:
        total = 0
        for ch in str(n):
            total += int(ch)
        n = total

    return n

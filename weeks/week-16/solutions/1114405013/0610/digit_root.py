def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total

    return n

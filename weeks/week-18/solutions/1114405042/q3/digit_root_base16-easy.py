def digit_root_base16(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    while n >= 16:
        s = 0
        while n:
            s += n % 16
            n //= 16
        n = s
    return n

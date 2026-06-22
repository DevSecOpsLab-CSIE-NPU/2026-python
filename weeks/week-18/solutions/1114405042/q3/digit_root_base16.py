BASE = 16

def digit_root_base16(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    return 1 + (n - 1) % (BASE - 1)

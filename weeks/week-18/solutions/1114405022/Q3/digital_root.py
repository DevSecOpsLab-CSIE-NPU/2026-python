def digital_root(x: int, base: int) -> int:
    if base == 0:
        return 0
    if x == 0:
        return 0

    while x >= base:
        digits_sum = 0
        temp_x = x
        while temp_x > 0:
            digits_sum += temp_x % base
            temp_x //= base
        x = digits_sum

    return x

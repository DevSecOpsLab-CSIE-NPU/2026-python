"""Q3 Digital Root in Arbitrary Base."""

import sys

VALID_BASES = {2, 3, 5, 6, 7, 8, 9, 11, 13, 16}


def _validate_base(base):
    if base not in VALID_BASES:
        raise ValueError("base must be one of 2, 3, 5, 6, 7, 8, 9, 11, 13, 16")


def to_base_digits(n, base):
    """將十進位非負整數轉成指定 base 的各位數字。"""
    _validate_base(base)
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return [0]

    digits = []
    current = n
    while current > 0:
        digits.append(current % base)
        current //= base
    return list(reversed(digits))


def digit_sum_in_base(n, base):
    """回傳 n 在指定 base 表示法中的位數和。"""
    return sum(to_base_digits(n, base))


def digital_root_in_base(n, base):
    """重複做 base 位數和，直到剩下一位數。"""
    _validate_base(base)
    if n < 0:
        raise ValueError("n must be non-negative")

    current = n
    while current >= base:
        current = digit_sum_in_base(current, base)
    return current


def solve(input_text, base=6):
    """讀取多行十進位非負整數直到 EOF。"""
    results = []
    for line in input_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        results.append(str(digital_root_in_base(int(stripped), base)))
    return "\n".join(results)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

def to_base_digits(n, base):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return list(reversed(digits))


def digit_root_in_base(x, base):
    if x == 0:
        return 0
    while x >= base:
        digits = to_base_digits(x, base)
        x = sum(digits)
    return x


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digit_root_in_base(x, base=8))


if __name__ == "__main__":
    main()

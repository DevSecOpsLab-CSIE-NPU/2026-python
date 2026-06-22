def to_base_str(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return "".join(reversed(digits))


def get_digital_root(x: int, base: int) -> int:
    if x == 0:
        return 0
    while x >= base:
        s = to_base_str(x, base)
        x = sum(int(ch) for ch in s)
    return x


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(get_digital_root(x, 5))


if __name__ == "__main__":
    main()

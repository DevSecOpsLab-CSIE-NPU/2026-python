ALLOWED_BASES = {2,3,5,6,7,8,9,10,11,13,16}

def digit_root_base_easy(value: int, base: int) -> int:

    if base not in ALLOWED_BASES:
        raise ValueError("base not supported")
    if value == 0:
        return 0
    current = value

    while current >= base:
        total = 0
        n = current
        # 逐位取餘相加
        while n > 0:
            total += n % base
            n //= base
        current = total
    return current


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python digit_root_base-easy-36.py <base>", file=sys.stderr)
        sys.exit(2)
    base = int(sys.argv[1])
    if base not in ALLOWED_BASES:
        print(f"Error: base must be one of {sorted(ALLOWED_BASES)}", file=sys.stderr)
        sys.exit(2)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        value = int(line)
        print(digit_root_base_easy(value, base))
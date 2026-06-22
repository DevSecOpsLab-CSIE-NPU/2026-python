def digit_root(x: int, base: int) -> int:
    while x >= base:
        total = 0
        while x > 0:
            total += x % base
            x //= base
        x = total
    return x


def solve_input(data: str, base: int) -> str:
    lines = data.strip().splitlines()
    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        results.append(str(digit_root(x, base)))
    return '\n'.join(results)


def main():
    import sys
    data = sys.stdin.read()
    sys.stdout.write(solve_input(data, 13))


if __name__ == '__main__':
    main()

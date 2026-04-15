import sys


def build_sequence(n: int, m: int) -> str:
    if n <= 1 or m <= 1:
        return "Boring!"

    sequence = [n]
    while n > 1:
        if n % m != 0:
            return "Boring!"
        n //= m
        sequence.append(n)
    return " ".join(str(value) for value in sequence)


def solve(data: str) -> str:
    outputs = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        outputs.append(build_sequence(n, m))
    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

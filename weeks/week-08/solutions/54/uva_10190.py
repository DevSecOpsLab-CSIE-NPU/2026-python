import sys


def build_sequence(n: int, m: int) -> str:
    if n <= 1 or m <= 1 or n > m:
        return "Boring!"

    seq = [m]
    while m != 1:
        if m % n != 0:
            return "Boring!"
        m //= n
        seq.append(m)

    return " ".join(map(str, seq))


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        out.append(build_sequence(n, m))
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

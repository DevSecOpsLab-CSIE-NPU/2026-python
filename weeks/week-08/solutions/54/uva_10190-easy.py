import sys


def solve(data: str) -> str:
    results: list[str] = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        n, m = map(int, line.split())

        if n <= 1 or m <= 1 or n > m:
            results.append("Boring!")
            continue

        seq = [str(m)]
        ok = True
        while m != 1:
            if m % n != 0:
                ok = False
                break
            m //= n
            seq.append(str(m))

        results.append(" ".join(seq) if ok else "Boring!")

    return "\n".join(results)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

def solve() -> None:
    import math
    import sys

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)
        out.append(str(total))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()

def solve() -> None:
    import math
    import sys

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        low = math.ceil(math.sqrt(a))
        high = math.floor(math.sqrt(b))
        count = max(0, high - low + 1)
        out.append(str(count))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()

import sys


def main() -> None:
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    t = values[0]
    i = 1
    out = []

    for _ in range(t):
        n = values[i]
        i += 1
        parties = values[i]
        i += 1

        seen = set()
        for _ in range(parties):
            h = values[i]
            i += 1

            d = h
            while d <= n:
                r = d % 7
                if r != 6 and r != 0:
                    seen.add(d)
                d += h

        out.append(str(len(seen)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

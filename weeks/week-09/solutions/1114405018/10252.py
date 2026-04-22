import sys


def solve(text):
    tokens = text.split()
    if not tokens:
        return ""

    it = iter(tokens)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        points = []
        xs = []
        ys = []
        for _ in range(n):
            x = int(next(it))
            y = int(next(it))
            points.append((x, y))
            xs.append(x)
            ys.append(y)

        xs.sort()
        ys.sort()

        # L1 距離的最優解就是 x、y 各自的中位數
        if n % 2 == 1:
            mx = xs[n // 2]
            my = ys[n // 2]
            count = 1
        else:
            lx, rx = xs[n // 2 - 1], xs[n // 2]
            ly, ry = ys[n // 2 - 1], ys[n // 2]
            mx = lx
            my = ly
            count = (rx - lx + 1) * (ry - ly + 1)

        best = 0
        for x, y in points:
            best += abs(x - mx) + abs(y - my)

        out.append(f"{best} {count}")

    return "\n".join(out) + "\n"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

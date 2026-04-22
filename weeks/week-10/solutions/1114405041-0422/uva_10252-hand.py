import sys


def solve(data):
    vals = [int(x) for x in data.split()]
    if not vals:
        return ""

    it = iter(vals)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))

        xs.sort()
        ys.sort()

        xl = xs[(n - 1) // 2]
        xr = xs[n // 2]
        yl = ys[(n - 1) // 2]
        yr = ys[n // 2]

        best = sum(abs(x - xl) for x in xs) + sum(abs(y - yl) for y in ys)
        ways = (xr - xl + 1) * (yr - yl + 1)
        out.append(f"{best} {ways}")

    return "\n".join(out)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

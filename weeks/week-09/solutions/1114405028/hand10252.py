# 手打版本
# 10252 的手打版本用中位數找到最佳整數點。

from typing import List


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        xs: List[int] = []
        ys: List[int] = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))

        xs.sort()
        ys.sort()

        if n % 2 == 1:
            x_low = x_high = xs[n // 2]
            y_low = y_high = ys[n // 2]
        else:
            x_low = xs[n // 2 - 1]
            x_high = xs[n // 2]
            y_low = ys[n // 2 - 1]
            y_high = ys[n // 2]

        dist = sum(abs(x - x_low) for x in xs) + sum(abs(y - y_low) for y in ys)
        ways = (x_high - x_low + 1) * (y_high - y_low + 1)
        out.append(f"{dist} {ways}")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == '__main__':
    solve()

# 10252 題目簡單版
# 直接用 x 與 y 座標的中位數求距離和最小值，並計算整數解個數。

from typing import List


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    outputs: List[str] = []

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

        distance = sum(abs(x - x_low) for x in xs) + sum(abs(y - y_low) for y in ys)
        count = (x_high - x_low + 1) * (y_high - y_low + 1)
        outputs.append(f"{distance} {count}")

    sys.stdout.write("\n".join(outputs) + ("\n" if outputs else ""))


if __name__ == "__main__":
    solve()

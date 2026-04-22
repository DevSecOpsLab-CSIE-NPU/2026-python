from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    這題是曼哈頓距離總和最小化：
    1. x 與 y 可以分開處理。
    2. 一維絕對值總和最小值在中位數區間。
    3. 若 n 是偶數，中位數區間可能有多個整數點，所以要算解的個數。
    """
    vals = [int(x) for x in data.split()]
    if not vals:
        return ""

    it = iter(vals)
    t = next(it)
    ans: list[str] = []

    for _ in range(t):
        n = next(it)
        xs: list[int] = []
        ys: list[int] = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))

        xs.sort()
        ys.sort()

        xl = xs[(n - 1) // 2]
        xr = xs[n // 2]
        yl = ys[(n - 1) // 2]
        yr = ys[n // 2]

        # 在中位數區間任選一點距離和都相同，直接用左端點計算即可。
        best = sum(abs(x - xl) for x in xs) + sum(abs(y - yl) for y in ys)
        ways = (xr - xl + 1) * (yr - yl + 1)

        ans.append(f"{best} {ways}")

    return "\n".join(ans)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

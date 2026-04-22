from __future__ import annotations

import sys


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""
    it = iter(nums)
    t = next(it)
    out: list[str] = []

    for _ in range(t):
        n = next(it)
        xs = [0] * n
        ys = [0] * n
        for i in range(n):
            xs[i] = next(it)
            ys[i] = next(it)

        xs.sort()
        ys.sort()

        x_left = xs[(n - 1) // 2]
        x_right = xs[n // 2]
        y_left = ys[(n - 1) // 2]
        y_right = ys[n // 2]

        min_dist = 0
        for x in xs:
            min_dist += abs(x - x_left)
        for y in ys:
            min_dist += abs(y - y_left)

        count = (x_right - x_left + 1) * (y_right - y_left + 1)
        out.append(f"{min_dist} {count}")

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

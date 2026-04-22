from __future__ import annotations

import sys


def solve_case(points: list[tuple[int, int]]) -> tuple[int, int]:
    # 曼哈頓距離可拆成 x 與 y 兩個獨立的一維問題。
    xs = sorted(x for x, _ in points)
    ys = sorted(y for _, y in points)

    lx = xs[(len(xs) - 1) // 2]
    rx = xs[len(xs) // 2]
    ly = ys[(len(ys) - 1) // 2]
    ry = ys[len(ys) // 2]

    best = sum(abs(x - lx) for x in xs) + sum(abs(y - ly) for y in ys)
    ways = (rx - lx + 1) * (ry - ly + 1)
    return best, ways


def main() -> None:
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    idx = 0
    t = nums[idx]
    idx += 1
    out: list[str] = []

    for _ in range(t):
        n = nums[idx]
        idx += 1
        points = []
        for _ in range(n):
            x = nums[idx]
            y = nums[idx + 1]
            idx += 2
            points.append((x, y))

        best, ways = solve_case(points)
        out.append(f"{best} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
"""
UVA 10908 — Largest Square 解決方案
給定字元網格和中心點，找最大同色正方形邊長。
"""

import sys


def find_largest_square_size(grid, center_r, center_c):
    """回傳以指定中心為中心的最大同色正方形邊長。"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    target_char = grid[center_r][center_c]
    k = 0

    while True:
        top = center_r - k
        bottom = center_r + k
        left = center_c - k
        right = center_c + k

        if top < 0 or left < 0 or bottom >= rows or right >= cols:
            break

        valid = True
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] != target_char:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            break

        k += 1

    return 2 * k - 1


def main():
    data = [line.rstrip("\n") for line in sys.stdin if line.strip() != ""]
    if not data:
        return

    it = iter(data)
    try:
        t = int(next(it))
    except StopIteration:
        return

    for _ in range(t):
        line = next(it)
        m, n, q = map(int, line.split())
        grid = [list(next(it)) for _ in range(m)]

        for _ in range(q):
            r, c = map(int, next(it).split())
            print(find_largest_square_size(grid, r, c))


if __name__ == "__main__":
    main()

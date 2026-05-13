"""
UVA 10908 - Largest Square

給定字元矩陣與查詢中心點，找以該點為中心、且內容全部同字元的最大奇數邊長正方形。
"""

from __future__ import annotations


def largest_square_size(grid: list[str], r: int, c: int) -> int:
    """使用逐層擴張法，只檢查新外框（perimeter）以提升效率。"""
    rows = len(grid)
    cols = len(grid[0])
    target = grid[r][c]

    radius = 0
    while True:
        next_radius = radius + 1
        top = r - next_radius
        bottom = r + next_radius
        left = c - next_radius
        right = c + next_radius

        # 只要超出邊界，就無法再擴張。
        if top < 0 or left < 0 or bottom >= rows or right >= cols:
            break

        ok = True

        # 檢查上邊與下邊。
        for col in range(left, right + 1):
            if grid[top][col] != target or grid[bottom][col] != target:
                ok = False
                break

        # 檢查左邊與右邊（角落雖可能重複檢查，但寫法清楚）。
        if ok:
            for row in range(top, bottom + 1):
                if grid[row][left] != target or grid[row][right] != target:
                    ok = False
                    break

        if not ok:
            break

        radius = next_radius

    return 2 * radius + 1


def solve_io(data: str) -> str:
    lines = data.strip().splitlines()
    if not lines:
        return ""

    idx = 0
    t = int(lines[idx].strip())
    idx += 1

    out: list[str] = []

    for _ in range(t):
        m, n, q = map(int, lines[idx].split())
        idx += 1

        grid = [lines[idx + i].rstrip("\n") for i in range(m)]
        idx += m

        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1
            out.append(str(largest_square_size(grid, r, c)))

    return "\n".join(out)


def main() -> None:
    import sys

    sys.stdout.write(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()

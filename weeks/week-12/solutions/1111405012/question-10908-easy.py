"""UVA 10908 - Largest Square（簡單版）"""

from __future__ import annotations

import sys


def square_fits(grid: list[list[str]], row: int, col: int, radius: int) -> bool:
    # 先算出這個半徑對應的邊界。
    top = row - radius
    bottom = row + radius
    left = col - radius
    right = col + radius

    # 超出網格範圍就直接失敗。
    if top < 0 or left < 0:
        return False
    if bottom >= len(grid) or right >= len(grid[0]):
        return False

    target = grid[row][col]
    for current_row in range(top, bottom + 1):
        for current_col in range(left, right + 1):
            if grid[current_row][current_col] != target:
                return False
    return True


def largest_square_side(grid: list[list[str]], row: int, col: int) -> int:
    # 從半徑 0 開始慢慢往外擴張。
    radius = 0
    while square_fits(grid, row, col, radius + 1):
        radius += 1
    return radius * 2 + 1


def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    pointer = 0
    case_count = int(data[pointer])
    pointer += 1
    outputs: list[str] = []

    for _ in range(case_count):
        rows = int(data[pointer])
        cols = int(data[pointer + 1])
        query_count = int(data[pointer + 2])
        pointer += 3

        grid = [list(data[pointer + row]) for row in range(rows)]
        pointer += rows

        outputs.append(f"{rows} {cols} {query_count}")

        for _ in range(query_count):
            row = int(data[pointer])
            col = int(data[pointer + 1])
            pointer += 2
            outputs.append(str(largest_square_side(grid, row, col)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()

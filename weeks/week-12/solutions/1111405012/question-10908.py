"""UVA 10908 - Largest Square"""

from __future__ import annotations

import sys


def square_fits(grid: list[list[str]], row: int, col: int, radius: int) -> bool:
    """檢查以指定中心與半徑形成的正方形是否全部同字元。"""

    center_char = grid[row][col]
    top = row - radius
    bottom = row + radius
    left = col - radius
    right = col + radius

    if top < 0 or left < 0 or bottom >= len(grid) or right >= len(grid[0]):
        return False

    for current_row in range(top, bottom + 1):
        for current_col in range(left, right + 1):
            if grid[current_row][current_col] != center_char:
                return False
    return True


def largest_square_side(grid: list[list[str]], row: int, col: int) -> int:
    """找出以該中心為核心的最大奇數邊長。"""

    radius = 0
    while square_fits(grid, row, col, radius + 1):
        radius += 1
    return radius * 2 + 1


def solve() -> None:
    """依題目格式輸出每筆測資與查詢結果。"""

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    index = 0
    case_count = int(tokens[index])
    index += 1
    outputs: list[str] = []

    for _ in range(case_count):
        rows = int(tokens[index])
        cols = int(tokens[index + 1])
        query_count = int(tokens[index + 2])
        index += 3

        grid = [list(tokens[index + row]) for row in range(rows)]
        index += rows

        outputs.append(f"{rows} {cols} {query_count}")

        for _ in range(query_count):
            row = int(tokens[index])
            col = int(tokens[index + 1])
            index += 2
            outputs.append(str(largest_square_side(grid, row, col)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()

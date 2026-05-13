"""
UVA 10908 - Largest Square
"""

from __future__ import annotations

import sys


def largest_square(grid: list[str], row: int, col: int) -> int:
    """從指定中心點向外擴張，找出最大奇數邊長正方形。"""
    rows = len(grid)
    cols = len(grid[0])
    target = grid[row][col]
    size = 1
    radius = 1

    while (
        row - radius >= 0
        and row + radius < rows
        and col - radius >= 0
        and col + radius < cols
    ):
        valid = True
        for r in range(row - radius, row + radius + 1):
            for c in range(col - radius, col + radius + 1):
                if grid[r][c] != target:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            break

        size = radius * 2 + 1
        radius += 1

    return size


def solve(data: str) -> str:
    """依題目格式輸出每組查詢的最大正方形邊長。"""
    lines = [line.rstrip("\n") for line in data.splitlines() if line.strip() != ""]
    if not lines:
        return ""

    index = 0
    cases = int(lines[index])
    index += 1
    outputs: list[str] = []

    for _ in range(cases):
        rows, cols, queries = map(int, lines[index].split())
        index += 1
        grid = lines[index : index + rows]
        index += rows

        outputs.append(f"{rows} {cols} {queries}")
        for _ in range(queries):
            row, col = map(int, lines[index].split())
            index += 1
            outputs.append(str(largest_square(grid, row, col)))

    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))

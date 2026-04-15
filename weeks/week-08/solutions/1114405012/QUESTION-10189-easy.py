"""UVA 10189 - Minesweeper（easy 版）

這版採最直覺作法：
對每一格，如果不是地雷，就直接檢查周圍 8 格地雷數量。
雖然看起來重複檢查較多，但程式非常好記。
"""

from __future__ import annotations

import sys


def count_neighbor_mines(grid: list[str], r: int, c: int) -> int:
    """計算 (r, c) 周圍 8 格的地雷數。"""
    n = len(grid)
    m = len(grid[0])
    total = 0

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                total += 1

    return total


def build_answer_easy(grid: list[str]) -> list[str]:
    """回傳單一盤面的答案。"""
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    out = []

    for r in range(n):
        row = []
        for c in range(m):
            if grid[r][c] == "*":
                row.append("*")
            else:
                row.append(str(count_neighbor_mines(grid, r, c)))
        out.append("".join(row))

    return out


def solve(raw_input: str) -> str:
    lines = raw_input.splitlines()
    i = 0
    case_id = 1
    blocks: list[str] = []

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        n, m = map(int, lines[i].split())
        i += 1
        if n == 0 and m == 0:
            break

        grid = lines[i:i + n]
        i += n

        ans = build_answer_easy(grid)
        blocks.append("\n".join([f"Field #{case_id}:"] + ans))
        case_id += 1

    return "\n\n".join(blocks)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

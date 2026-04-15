"""UVA 10189 - Minesweeper（手打版）

手打思路：
1. 讀每個測資的 n, m。
2. 對每格判斷：
   - 如果是 *，直接放 *。
   - 如果是 .，就手動掃 8 個方向數地雷。
3. 輸出 Field #k，測資間空一行。
"""

from __future__ import annotations

import sys


def count_around_mines(board: list[str], row: int, col: int) -> int:
    """數 (row, col) 周圍 8 格地雷數。"""
    n = len(board)
    m = len(board[0])
    total = 0

    # 8 個方向，手打最直觀。
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "*":
            total += 1

    return total


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    case_no = 1
    blocks: list[str] = []

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        n, m = map(int, lines[i].split())
        i += 1

        if n == 0 and m == 0:
            break

        board = lines[i:i + n]
        i += n

        out_grid: list[str] = []
        for r in range(n):
            row_chars: list[str] = []
            for c in range(m):
                if board[r][c] == "*":
                    row_chars.append("*")
                else:
                    mines = count_around_mines(board, r, c)
                    row_chars.append(str(mines))
            out_grid.append("".join(row_chars))

        one_case = [f"Field #{case_no}:"] + out_grid
        blocks.append("\n".join(one_case))
        case_no += 1

    return "\n\n".join(blocks)


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        return
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()

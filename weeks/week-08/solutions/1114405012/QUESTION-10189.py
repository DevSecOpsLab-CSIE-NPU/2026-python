"""UVA 10189 - Minesweeper

正式版：以地雷為中心，對周圍 8 格做累加。
"""

from __future__ import annotations

import sys


def build_field_answer(grid: list[str]) -> list[str]:
    """將單一地雷盤面轉成答案盤面。"""
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0

    counts = [[0] * m for _ in range(n)]

    # 以每顆地雷為中心更新 8 個方向，時間複雜度 O(n*m)。
    for r in range(n):
        for c in range(m):
            if grid[r][c] != "*":
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "*":
                        counts[nr][nc] += 1

    result = []
    for r in range(n):
        row_chars = []
        for c in range(m):
            if grid[r][c] == "*":
                row_chars.append("*")
            else:
                row_chars.append(str(counts[r][c]))
        result.append("".join(row_chars))
    return result


def solve(raw_input: str) -> str:
    lines = raw_input.splitlines()
    idx = 0
    field_no = 1
    blocks: list[str] = []

    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        n, m = map(int, lines[idx].split())
        idx += 1
        if n == 0 and m == 0:
            break

        grid = lines[idx:idx + n]
        idx += n

        answer_grid = build_field_answer(grid)

        block_lines = [f"Field #{field_no}:"] + answer_grid
        blocks.append("\n".join(block_lines))
        field_no += 1

    return "\n\n".join(blocks)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

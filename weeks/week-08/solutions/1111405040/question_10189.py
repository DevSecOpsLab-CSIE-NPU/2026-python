"""
UVA 10189: Minesweeper
"""

from __future__ import annotations

import sys


NEIGHBOR_OFFSETS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)


def count_adjacent_mines(field: list[str], row: int, col: int) -> int:
    """計算指定格子周圍 8 個方向的地雷數量。"""
    rows = len(field)
    cols = len(field[0]) if rows else 0
    total = 0

    for row_offset, col_offset in NEIGHBOR_OFFSETS:
        next_row = row + row_offset
        next_col = col + col_offset

        if 0 <= next_row < rows and 0 <= next_col < cols:
            if field[next_row][next_col] == "*":
                total += 1

    return total


def solve_field(field: list[str]) -> list[str]:
    """把單一地雷盤面轉成數字盤面。"""
    result: list[str] = []

    for row_index, row in enumerate(field):
        output_row: list[str] = []

        for col_index, char in enumerate(row):
            if char == "*":
                output_row.append("*")
            else:
                output_row.append(str(count_adjacent_mines(field, row_index, col_index)))

        result.append("".join(output_row))

    return result


def solve(text: str) -> str:
    """處理多組 Minesweeper 輸入。"""
    lines = text.splitlines()
    index = 0
    case_number = 1
    outputs: list[str] = []

    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line:
            continue

        rows, cols = map(int, line.split())
        if rows == 0 and cols == 0:
            break

        field = lines[index:index + rows]
        index += rows

        outputs.append(f"Field #{case_number}:")
        outputs.extend(solve_field(field))
        case_number += 1

    return "\n\n".join(
        "\n".join(block.splitlines()) for block in _split_blocks(outputs)
    )


def _split_blocks(lines: list[str]) -> list[str]:
    """把 Field 標題與盤面整理成多個輸出區塊。"""
    blocks: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        if line.startswith("Field #") and current:
            blocks.append(current)
            current = []
        current.append(line)

    if current:
        blocks.append(current)

    return ["\n".join(block) for block in blocks]


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

"""UVA 11349 - Symmetric Matrix.

這是更容易記憶的版本，直接用 `all(...)` 一次完成判斷。
"""

from __future__ import annotations

import sys


def parse_matrix_size(line: str) -> int:
    return int(line.split("=")[1])


def is_symmetric_matrix(matrix: list[list[int]]) -> bool:
    """只要有一個元素是負數，或中心對稱失敗，就回傳 False。"""

    size = len(matrix)
    return all(
        matrix[row_index][col_index] >= 0
        and matrix[row_index][col_index] == matrix[size - 1 - row_index][size - 1 - col_index]
        for row_index in range(size)
        for col_index in range(size)
    )


def solve(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    test_count = int(lines[0])
    line_index = 1
    answers: list[str] = []

    for case_number in range(1, test_count + 1):
        size = parse_matrix_size(lines[line_index])
        line_index += 1

        matrix = [list(map(int, lines[line_index + offset].split())) for offset in range(size)]
        line_index += size

        verdict = "Symmetric." if is_symmetric_matrix(matrix) else "Non-symmetric."
        answers.append(f"Test #{case_number}: {verdict}")

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
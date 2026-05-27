"""UVA 11349 - Symmetric Matrix.

這個版本保留較完整的步驟拆解，方便直接手打與檢查。
"""

from __future__ import annotations

import sys


def parse_matrix_size(line: str) -> int:
    """從 `N = 3` 這種格式中取出矩陣大小。"""

    return int(line.split("=")[1])


def is_symmetric_matrix(matrix: list[list[int]]) -> bool:
    """判斷矩陣是否同時符合：非負、中心對稱。"""

    size = len(matrix)

    # 先確認所有元素都不是負數。
    for row in matrix:
        for value in row:
            if value < 0:
                return False

    # 再檢查中心對稱：左上角要對到右下角。
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] != matrix[size - 1 - row_index][size - 1 - col_index]:
                return False

    return True


def solve(text: str) -> str:
    """把輸入文字轉成題目的輸出格式。"""

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    test_count = int(lines[0])
    line_index = 1
    answers: list[str] = []

    for case_number in range(1, test_count + 1):
        size = parse_matrix_size(lines[line_index])
        line_index += 1

        matrix: list[list[int]] = []
        for _ in range(size):
            matrix.append(list(map(int, lines[line_index].split())))
            line_index += 1

        verdict = "Symmetric." if is_symmetric_matrix(matrix) else "Non-symmetric."
        answers.append(f"Test #{case_number}: {verdict}")

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
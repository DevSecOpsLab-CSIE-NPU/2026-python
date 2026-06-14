"""UVA 11349 - Symmetric Matrix.

輸入格式會是多組測資，每組先給矩陣大小，再給 n 行矩陣內容。
本題的對稱定義是「中心對稱」，而且所有元素都必須是非負數。
"""

from __future__ import annotations

import re
import sys
from typing import Iterable


def is_symmetric_matrix(matrix: list[list[int]]) -> bool:
    """判斷矩陣是否為題目定義的對稱矩陣。"""

    size = len(matrix)
    for row in matrix:
        if len(row) != size:
            return False

    for row_index in range(size):
        for col_index in range(size):
            value = matrix[row_index][col_index]
            if value < 0:
                return False
            if value != matrix[size - 1 - row_index][size - 1 - col_index]:
                return False
    return True


def parse_size(line: str) -> int:
    """從 `N = 3` 這類字串中抓出矩陣大小。"""

    match = re.search(r"-?\d+", line)
    if match is None:
        raise ValueError(f"無法解析矩陣大小：{line!r}")
    return int(match.group())


def solve(lines: Iterable[str]) -> list[str]:
    data = [line.strip() for line in lines if line.strip()]
    if not data:
        return []

    case_count = int(data[0])
    cursor = 1
    answers: list[str] = []

    for case_number in range(1, case_count + 1):
        size = parse_size(data[cursor])
        cursor += 1

        matrix: list[list[int]] = []
        for _ in range(size):
            matrix.append([int(token) for token in data[cursor].split()])
            cursor += 1

        verdict = "Symmetric." if is_symmetric_matrix(matrix) else "Non-symmetric."
        answers.append(f"Test #{case_number}: {verdict}")

    return answers


def main() -> None:
    output = solve(sys.stdin)
    sys.stdout.write("\n".join(output))
    if output:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
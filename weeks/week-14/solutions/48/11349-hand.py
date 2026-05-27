"""UVA 11349 - Symmetric Matrix.

手打版：把判斷拆得更直白，方便現場逐行輸入。
"""

from __future__ import annotations

import sys


def parse_size(text: str) -> int:
    """從 `N = 3` 這種字串取出 3。"""

    return int(text.split("=")[1])


def is_symmetric(matrix: list[list[int]]) -> bool:

    n = len(matrix)

    for row in matrix:
        for value in row:
            if value < 0:
                return False

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False

    return True


def solve(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    index = 1
    result: list[str] = []

    for case_no in range(1, t + 1):
        n = parse_size(lines[index])
        index += 1

        matrix: list[list[int]] = []
        for _ in range(n):
            row = list(map(int, lines[index].split()))
            matrix.append(row)
            index += 1

        if is_symmetric(matrix):
            result.append(f"Test #{case_no}: Symmetric.")
        else:
            result.append(f"Test #{case_no}: Non-symmetric.")

    return "\n".join(result)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
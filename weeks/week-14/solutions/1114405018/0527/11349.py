"""UVA 11349 - Symmetric Matrix.

題目要求判斷矩陣是否同時滿足兩個條件：
1. 所有元素都必須是非負數。
2. 矩陣要關於中心點對稱，也就是 M[i][j] 必須等於 M[n-1-i][n-1-j]。

這個版本直接從輸入中擷取所有整數，因為題目格式中的 `N = n`
和矩陣內容都可以安全地用數字解析。
"""

from __future__ import annotations

import re
import sys


def is_symmetric_matrix(matrix: list[list[int]]) -> bool:
    # 先確認所有數值都不是負數，這是題目的第一個必要條件。
    for row in matrix:
        for value in row:
            if value < 0:
                return False

    n = len(matrix)
    # 再逐一比對每個位置和它的中心對稱位置是否相同。
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve() -> None:
    raw_input = sys.stdin.read()
    if not raw_input.strip():
        return

    # 題目輸入包含 `N = 3` 這種格式，因此直接擷取全部整數最穩定。
    numbers = list(map(int, re.findall(r"-?\d+", raw_input)))
    if not numbers:
        return

    case_count = numbers[0]
    index = 1
    results: list[str] = []

    for case_id in range(1, case_count + 1):
        n = numbers[index]
        index += 1

        matrix: list[list[int]] = []
        for _ in range(n):
            row = numbers[index:index + n]
            index += n
            matrix.append(row)

        verdict = "Symmetric." if is_symmetric_matrix(matrix) else "Non-symmetric."
        results.append(f"Test #{case_id}: {verdict}")

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
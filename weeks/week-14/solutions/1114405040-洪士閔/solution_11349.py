"""
UVA 11349 - Symmetric Matrix

題目重點：
給一個 n x n 矩陣，判斷它是不是題目定義的 Symmetric Matrix。
這裡的對稱不是一般數學上的 M[i][j] == M[j][i]，
而是以整個矩陣中心為基準，左上角要對到右下角、第二個數要對到倒數第二個數。

判斷條件：
1. 矩陣裡所有數字都必須 >= 0。
2. 把矩陣依照輸入順序攤平成一維串列後，必須和反轉後的串列完全相同。
"""

import sys
from typing import Iterable, List, TextIO


def is_symmetric_matrix(matrix: List[List[int]]) -> bool:
    """判斷一個矩陣是否符合 UVA 11349 的對稱規則。"""
    n = len(matrix)
    if n == 0:
        return False

    values = []

    for row in matrix:
        # 題目保證是 n x n，但函式本身也多檢查一次，讓測試更安全。
        if len(row) != n:
            return False

        for value in row:
            # 只要出現負數，就一定不是 Symmetric。
            if value < 0:
                return False

            # 將矩陣由左到右、由上到下攤平成一維串列。
            values.append(value)

    # 若一維串列和反轉後一樣，代表頭尾位置完全對稱。
    return values == values[::-1]


def solve(input_stream: TextIO = sys.stdin) -> str:
    """讀取完整輸入，回傳所有測資的答案字串。"""
    lines = iter(input_stream.read().splitlines())
    test_count = int(next(lines).strip())
    output = []

    for case_number in range(1, test_count + 1):
        # 每筆測資的第一行格式是「N = n」，例如：N = 3。
        header = next_non_empty_line(lines)

        # split("=") 後取右邊的 n，再轉成整數。
        n = int(header.split("=")[1].strip())

        # 接下來讀入 n 行，每行都有 n 個整數。
        matrix = [list(map(int, next(lines).split())) for _ in range(n)]

        if is_symmetric_matrix(matrix):
            result = "Symmetric."
        else:
            result = "Non-symmetric."

        output.append(f"Test #{case_number}: {result}")

    return "\n".join(output)


def next_non_empty_line(lines: Iterable[str]) -> str:
    """略過空白行，取得下一行真正有內容的輸入。"""
    for line in lines:
        line = line.strip()
        if line:
            return line

    raise ValueError("Missing test case header")


if __name__ == "__main__":
    print(solve())

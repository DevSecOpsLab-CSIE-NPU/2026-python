"""
UVA 299 - Train Swapping（正式版）

題意：
要把車廂排列成遞增順序，且每次只能交換「相鄰」兩節車廂。
問最少要交換幾次。

核心觀念：
最少相鄰交換次數 = 反序數（inversion count）。
反序數定義：
在陣列中，若 i < j 但 a[i] > a[j]，則 (i, j) 是一組反序。
"""

from __future__ import annotations

from typing import List


def count_inversions(cars: List[int]) -> int:
    """
    計算車廂序列的反序數。

    這裡使用 O(n^2) 雙迴圈，
    因為題目 L <= 50，資料量很小，寫法直觀且容易驗證。
    """
    swaps = 0
    n = len(cars)

    for i in range(n):
        for j in range(i + 1, n):
            if cars[i] > cars[j]:
                swaps += 1

    return swaps


def format_answer(swaps: int) -> str:
    """依題目格式輸出答案字串。"""
    return f"Optimal train swapping takes {swaps} swaps."


def solve_text(text: str) -> str:
    """
    解析整份輸入並回傳整份輸出。

    輸入格式：
    - 第一行：測資數 N
    - 每組測資兩行：
      1) L
      2) L 個整數（車廂排列）
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    idx = 1
    out = []

    for _ in range(t):
        l = int(lines[idx])
        idx += 1

        # 即使 l=0，這行也可能是空，保守處理
        arr = []
        if l > 0:
            arr = list(map(int, lines[idx].split()))
            idx += 1

        swaps = count_inversions(arr)
        out.append(format_answer(swaps))

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_text(data))

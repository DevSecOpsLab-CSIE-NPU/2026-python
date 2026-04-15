"""
UVA 299 - Train Swapping（正式版）

題意摘要：
  給定一列車廂排列，允許的操作是「交換相鄰兩節車廂」。
  目標是把車廂排成遞增順序（1..L），並求最少交換次數。

核心觀念：
  最少相鄰交換次數 = 反序數（inversion count）。
  反序數定義為：
    對所有 i < j，若 a[i] > a[j]，就算一組反序。

由於題目限制 L <= 50，使用 O(L^2) 雙層迴圈即可通過。
"""

from __future__ import annotations

import sys


def min_adjacent_swaps(train: list[int]) -> int:
    """
    計算車廂序列排序成遞增所需最少相鄰交換次數。

    :param train: 車廂排列
    :return: 最少交換次數
    """
    swaps = 0
    n = len(train)

    for i in range(n):
        for j in range(i + 1, n):
            if train[i] > train[j]:
                swaps += 1

    return swaps


def format_output(swaps: int) -> str:
    """依題目格式輸出答案字串。"""
    return f"Optimal train swapping takes {swaps} swaps."


def solve_case(train: list[int]) -> str:
    """單筆測資求解。"""
    return format_output(min_adjacent_swaps(train))


def main() -> None:
    """
    讀取輸入格式：
      第一行 N（測資筆數）
      每筆測資：
        一行 L
        一行 L 個整數（車廂排列）
    並逐筆輸出答案。
    """
    first = sys.stdin.readline().strip()
    if not first:
        return

    t = int(first)
    for _ in range(t):
        # 讀取 L（長度）
        line = sys.stdin.readline().strip()
        while line == "":
            line = sys.stdin.readline().strip()
        _l = int(line)

        # 讀取車廂排列
        train_line = sys.stdin.readline().strip()
        while train_line == "":
            train_line = sys.stdin.readline().strip()
        train = list(map(int, train_line.split()))

        print(solve_case(train))


if __name__ == "__main__":
    main()

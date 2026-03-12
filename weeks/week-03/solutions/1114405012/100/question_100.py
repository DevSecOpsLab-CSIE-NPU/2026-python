"""
UVA 100 - The 3n+1 Problem（正式版）

說明：
給定兩個正整數 i, j，找出區間 [min(i, j), max(i, j)] 內，
哪個數的 Collatz cycle length 最大，並輸出 i j max_cycle。

Cycle Length 定義：
從 n 開始，反覆執行：
- n 是奇數 -> n = 3*n + 1
- n 是偶數 -> n = n // 2
直到 n == 1 為止。
「經過的節點數量（包含起點 n 與終點 1）」就是 cycle length。
"""

from __future__ import annotations

from typing import Dict

# 記憶化快取：把「已算過的 n 對應 cycle length」存起來，避免重複計算
# 先放入最基本的已知值：1 的 cycle length 一定是 1
_MEMO: Dict[int, int] = {1: 1}


def cycle_length(n: int) -> int:
    """
    回傳正整數 n 的 Collatz cycle length。

    實作重點：
    1) 先沿著 Collatz 規則往下走，直到遇到已知答案（命中 _MEMO）。
    2) 再把走過的路徑反向回填長度，讓下次查詢更快。

    例如：n = 22
    22 -> 11 -> 34 -> ... -> 1，cycle length = 16
    """
    if n <= 0:
        raise ValueError("n 必須是正整數")

    # path 用來記錄這次尚未命中快取前走過的節點
    path = []
    current = n

    # 一路走到遇到已知答案（通常會到 1 或中途命中快取）
    while current not in _MEMO:
        path.append(current)
        if current % 2 == 1:  # 奇數
            current = 3 * current + 1
        else:  # 偶數
            current = current // 2

    # 目前 current 已命中快取，base_len 是 current 的已知長度
    base_len = _MEMO[current]

    # 反向回填：距離已知節點越近者，長度越小
    # 例如 path = [22, 11, 34]，且 17 命中，
    # 則 34 的長度 = base+1，11 = base+2，22 = base+3
    for value in reversed(path):
        base_len += 1
        _MEMO[value] = base_len

    return _MEMO[n]


def max_cycle_length_in_range(i: int, j: int) -> int:
    """
    計算區間 [min(i, j), max(i, j)] 的最大 cycle length。

    注意：
    題目要求輸入順序可顛倒，所以實作時要先正規化區間。
    """
    if i <= 0 or j <= 0:
        raise ValueError("i, j 必須是正整數")

    left, right = (i, j) if i <= j else (j, i)
    max_cycle = 0

    for n in range(left, right + 1):
        length = cycle_length(n)
        if length > max_cycle:
            max_cycle = length

    return max_cycle


def solve_pair(i: int, j: int) -> str:
    """
    依 UVA 100 格式輸出單筆答案："i j max_cycle"。

    這裡會保留原始輸入順序 i, j，不會交換位置。
    """
    return f"{i} {j} {max_cycle_length_in_range(i, j)}"


def solve_text(text: str) -> str:
    """
    批次處理多行輸入文字，回傳多行輸出。

    輸入格式：
    每行兩個整數，例如：
    1 10
    100 200

    輸出格式：
    每行對應一筆 "i j max_cycle"
    """
    output_lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        i_str, j_str = line.split()
        i, j = int(i_str), int(j_str)
        output_lines.append(solve_pair(i, j))
    return "\n".join(output_lines)


def reset_memo() -> None:
    """提供給測試使用：重設快取到初始狀態。"""
    _MEMO.clear()
    _MEMO[1] = 1


if __name__ == "__main__":
    # 從標準輸入讀到 EOF，並輸出所有答案
    # 使用方式：
    # python question_100.py < input.txt
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_text(data))

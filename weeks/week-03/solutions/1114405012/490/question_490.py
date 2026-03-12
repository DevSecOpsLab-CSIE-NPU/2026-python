"""
UVA 490 - Rotating Sentences（正式版）

題意：
把輸入文字視為一個由多行組成的矩陣，做「順時針 90 度旋轉」。

重點規則：
1. 最後一行輸入會變成最左邊直行。
2. 第一行輸入會變成最右邊直行。
3. 各行長度不一時，短行視為右側補空白。
4. 輸出每行右側多餘補白可去除（避免不必要尾端空格）。
"""

from __future__ import annotations


def rotate_90_clockwise(lines: list[str]) -> list[str]:
    """
    將文字行列順時針旋轉 90 度，回傳旋轉後的行列表。

    作法：
    - 先找最長行長 max_len
    - 新矩陣共有 max_len 列
    - 第 r 列由「原本各行的第 r 欄」從下往上組成
    """
    if not lines:
        return []

    max_len = max(len(line) for line in lines)
    rotated = []

    for col in range(max_len):
        row_chars = []

        # 從原輸入最後一行往第一行讀，形成順時針旋轉
        for line in reversed(lines):
            if col < len(line):
                row_chars.append(line[col])
            else:
                row_chars.append(" ")

        # 去掉右側補空白，保留必要的前導空白
        rotated.append("".join(row_chars).rstrip())

    return rotated


def solve_text(text: str) -> str:
    """處理完整輸入文字，回傳完整輸出文字。"""
    # splitlines() 會保留中間空行（作為空字串），符合本題矩陣概念
    lines = text.splitlines()
    rotated = rotate_90_clockwise(lines)
    return "\n".join(rotated)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data:
        print(solve_text(data), end="")

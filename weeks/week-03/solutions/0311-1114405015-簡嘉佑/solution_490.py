"""
UVA 490 - Rotating Sentences

題意說明：
  讀取若干行文字，將整個文字方塊順時針旋轉 90 度後輸出。

  旋轉規則：
    - 原始最後一行 → 輸出最左側（第 0 欄）
    - 原始第一行   → 輸出最右側（最後一欄）
    - 若各行長度不同，以空白補齊成矩形後再旋轉

  輸出規則：
    - 每個旋轉後的「欄」輸出為一行，不去掉尾端空白
    - 行與行之間以換行分隔

演算法概要：
  1. 找出所有行中最大長度 max_len。
  2. 每行以 ljust 補齊右側空白到 max_len，形成矩形。
  3. 逐欄讀取：第 col 欄由最後一行到第一行組合成新的一行。
  4. 輸出所有新行。
"""

from __future__ import annotations

import sys


# ===========================================================
# 核心函式
# ===========================================================

def rotate_90_clockwise(lines: list[str]) -> list[str]:
    """
    將文字行陣列順時針旋轉 90 度。

    :param lines: 原始輸入的每一行（不含換行字元）
    :return: 旋轉後每一行組成的串列

    詳細步驟：
      1. 計算最長行的寬度 max_len。
      2. 所有行以空白補齊到 max_len（ljust 補右側），形成矩形。
      3. 針對每個欄索引 col（0 到 max_len-1）：
         從最後一行到第一行逐格取出 padded[row][col]，
         串接成新的輸出行。
      4. 回傳所有新行。
    """
    if not lines:
        return []

    # 找最大行寬，以便補齊較短的行
    max_len = max(len(line) for line in lines)

    # 每行右側補空白到 max_len，形成等寬矩形
    padded = [line.ljust(max_len, " ") for line in lines]

    result: list[str] = []
    for col in range(max_len):
        # 由最後一行（row = len-1）往第一行（row = 0）讀取第 col 個字元
        # 這樣讀出的順序正是順時針旋轉 90 度的效果
        out_line = "".join(padded[row][col] for row in range(len(padded) - 1, -1, -1))
        result.append(out_line)

    return result


def format_output(lines: list[str]) -> str:
    """
    將旋轉後的行串列組合成最終輸出字串。

    :param lines: 旋轉後每一行的串列
    :return: 以換行字元連接的完整輸出字串
    """
    return "\n".join(lines)


# ===========================================================
# 主程式入口
# ===========================================================

def main() -> None:
    """
    讀取標準輸入的所有行（去除換行符號後），
    執行 90 度順時針旋轉，再輸出結果。
    """
    # 讀取所有輸入行，去除結尾換行符號
    lines = [line.rstrip("\n") for line in sys.stdin]

    # 若輸入為空，直接結束
    if not lines:
        return

    # 旋轉並輸出
    rotated = rotate_90_clockwise(lines)
    print(format_output(rotated))


if __name__ == "__main__":
    main()

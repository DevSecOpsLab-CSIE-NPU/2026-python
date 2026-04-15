"""
UVA 10035 - 加法進位次數（正式版）

題意摘要：
  計算兩個正整數相加時，總共發生幾次「進位（carry）」。
  輸出格式：
    0 次 → "No carry operation."
    1 次 → "1 carry operation."
    N 次 → "N carry operations."
  兩個 0 代表輸入結束，不輸出任何結果。

解法：
  模擬直式加法，由個位開始逐位計算：
    total = 個位相加 + 上一輪進位
    本輪進位 = total // 10
    若本輪進位 > 0，計數 +1
  直到兩數都為 0 且無剩餘進位。
"""

from __future__ import annotations

import sys


def count_carries(a: int, b: int) -> int:
    """
    計算 a + b 時發生的進位次數。

    :param a: 第一個非負整數
    :param b: 第二個非負整數
    :return:  進位次數
    """
    carries = 0   # 進位次數計數器
    carry   = 0   # 當前進位值（0 或 1）

    while a > 0 or b > 0 or carry > 0:
        total   = (a % 10) + (b % 10) + carry   # 個位相加
        carry   = total // 10                    # 是否產生進位
        if carry:
            carries += 1     # 有進位，計數加 1
        a //= 10             # 移除已處理的個位
        b //= 10

    return carries


def format_result(carries: int) -> str:
    """
    將進位次數格式化為題目要求的輸出字串。

    :param carries: 進位次數
    :return:        "No carry operation." / "1 carry operation." / "N carry operations."
    """
    if carries == 0:
        return "No carry operation."
    elif carries == 1:
        return "1 carry operation."
    else:
        return f"{carries} carry operations."


def main() -> None:
    """讀取標準輸入，遇到 0 0 結束，每組輸出進位次數。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:   # 結束條件
            break
        print(format_result(count_carries(a, b)))


if __name__ == "__main__":
    main()

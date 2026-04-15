"""
UVA 10035 - 加法進位次數（easy 版）

簡單記法：
  把兩個數字的每一位「由右到左」一位一位相加，
  看看有幾次「相加結果 >= 10」（代表有進位）。

核心步驟：
  1. 取出 a 和 b 的個位：a % 10、b % 10
  2. 三者相加：個位_a + 個位_b + carry（上一輪的進位）
  3. 若總和 >= 10 → 產生進位，計數 +1，carry = 1；否則 carry = 0
  4. a //= 10、b //= 10（去掉已處理的個位）
  5. 重複直到 a = b = carry = 0

輸出格式：
  攜帶次數 0    → "No carry operation."
  攜帶次數 1    → "1 carry operation."    （注意：operation 無 s）
  攜帶次數 >= 2 → "N carry operations."   （注意：operations 有 s）
"""

from __future__ import annotations

import sys


def carries(a: int, b: int) -> int:
    """
    計算 a + b 的進位次數。

    :param a: 第一個非負整數
    :param b: 第二個非負整數
    :return:  進位次數

    簡單記法：
      count = 0        # 計數進位次數
      c     = 0        # 上一輪進位值（0 或 1）
      每輪：
        s = a%10 + b%10 + c   → 本位相加（含進位）
        c = s // 10           → 新進位（1 或 0）
        if c: count += 1      → 有進位就計數
        a //= 10; b //= 10    → 移到下一位
    """
    count = 0
    c     = 0   # 進位值

    while a or b or c:
        # 本位三數相加：a 個位 + b 個位 + 前一輪進位
        s = a % 10 + b % 10 + c
        # 計算本輪是否產生進位（>= 10 就進位）
        c = s // 10
        # 有進位就累加計數
        if c:
            count += 1
        # 移除已處理的個位
        a //= 10
        b //= 10

    return count


def fmt(n: int) -> str:
    """
    依進位次數回傳對應的輸出字串。

    :param n: 進位次數
    :return:  題目要求的輸出格式

    記憶訣竅：
      0 次 → No carry operation.   （No 開頭）
      1 次 → 1 carry operation.    （operation，無 s）
      多次 → N carry operations.   （operations，有 s）
    """
    if n == 0:
        return "No carry operation."
    if n == 1:
        return "1 carry operation."
    return f"{n} carry operations."


def main() -> None:
    """讀取輸入，遇到 0 0 停止，依序輸出每組的進位次數。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:   # 輸入結束條件
            break
        print(fmt(carries(a, b)))


if __name__ == "__main__":
    main()

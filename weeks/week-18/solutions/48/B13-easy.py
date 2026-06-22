"""
Base-13 數字根 (Digital Root) — AI 詳細註解版

功能：
    將輸入的十進位非負整數轉為 13 進位，
    反覆計算各位數之和直到剩一位數（< 13），
    以十進位輸出該數字根。
    輸入 0 則直接輸出 0。

時間複雜度：O(log₁₃ x)，每次拆位最多 log₁₃ x 次
空間複雜度：O(1)，僅使用常數變數
"""

import sys

BASE = 13


def digital_root(n: int) -> int:
    """計算 base=13 的數字根（反覆加總位數到 < BASE）。"""
    if n == 0:
        return 0
    while n >= BASE:
        s = 0
        while n > 0:
            s += n % BASE
            n //= BASE
        n = s
    return n


def main():
    """讀取 stdin 每行數字，輸出其 base-13 數字根。"""
    for line in sys.stdin.read().splitlines():
        line = line.strip()
        if not line:
            continue
        print(digital_root(int(line)))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
解題模組：UVA 11461 — Square Numbers

功能：
- `count_square_numbers(a, b)`：計算閉區間 [a, b] 內完全平方數的個數
- `main()`：從標準輸入讀取多組測資，並依題目格式輸出結果

繁體中文說明：
完全平方數是指可以寫成 k^2 的正整數，例如 1、4、9、16。
本題只要找到區間內第一個與最後一個完全平方數，再計算它們之間有幾個平方數即可。

作法：
1. 使用 `math.isqrt(x)` 取得 x 的整數平方根。
2. 找到不小於 a 的第一個平方數：
   - 先取 `low = isqrt(a)`，如果 `low^2 < a`，就把 low 加 1。
3. 找到不大於 b 的最後一個平方數：
   - 直接取 `high = isqrt(b)`。
4. 答案就是 `high - low + 1`，若結果小於 0，則回傳 0。

時間複雜度：O(1)
空間複雜度：O(1)
"""
import math
import sys


def count_square_numbers(a: int, b: int) -> int:
    """計算閉區間 [a, b] 中完全平方數的個數。

    參數：
    - a: 區間左端點
    - b: 區間右端點

    回傳：
    - int：區間內完全平方數數量
    """
    if a > b:
        return 0

    # 找到第一個大於等於 a 的平方數對應根值
    low = math.isqrt(a)
    if low * low < a:
        low += 1

    # 找到最後一個小於等於 b 的平方數對應根值
    high = math.isqrt(b)

    # 兩端根值的數量差即為平方數個數
    return max(0, high - low + 1)


def main() -> None:
    """讀取多組 a, b，直到遇到 0 0 結束。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    for a_s, b_s in zip(it, it):
        a = int(a_s)
        b = int(b_s)
        if a == 0 and b == 0:
            break
        print(count_square_numbers(a, b))


if __name__ == '__main__':
    main()

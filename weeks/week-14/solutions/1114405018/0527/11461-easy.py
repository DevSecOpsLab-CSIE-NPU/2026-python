"""UVA 11461 - Square Numbers (easy version).

繁體中文詳細說明：

題目目標：給定多組整數 a, b（1 ≤ a ≤ b ≤ 100000），計算閉區間 [a, b]
中有多少個完全平方數（perfect square）。輸入以多行給出，最後以
"0 0" 作為結束標記。

解法核心：若 x 是完全平方數，則存在 k 使得 x = k*k。要計算 [a, b]
中共有多少個這樣的 x，只要看 k 的範圍：k 必須滿足 k^2 ≥ a 且 k^2 ≤ b，
因此 k 的整數範圍是：ceil(sqrt(a)) .. floor(sqrt(b))。計算個數可以用
floor(sqrt(b)) - floor(sqrt(a-1))（使用整數平方根函數 `math.isqrt` 更精準）。

本檔以最簡潔且易背的方式實作：對每一行輸入解析 a,b，若為終止值則跳出，
否則計算並輸出結果。
"""

from __future__ import annotations

import math
import sys


def solve() -> None:
    """主程式：讀取 stdin，逐行處理每一組 a, b，計算並輸出結果。"""

    results: list[str] = []

    for line in sys.stdin:
        # 解析該行的兩個整數 a, b
        a, b = map(int, line.split())
        # 遇到終止條件 "0 0" 時結束處理
        if a == 0 and b == 0:
            break

        # 使用 math.isqrt 取得不大於平方根的最大整數值
        # 區間內平方數的個數 = isqrt(b) - isqrt(a-1)
        count = math.isqrt(b) - math.isqrt(a - 1)
        results.append(str(count))

    # 一次性輸出所有結果，每個結果一行
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()

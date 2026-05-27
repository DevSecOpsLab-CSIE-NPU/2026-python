"""UVA 11417 - GCD (easy version).

簡短說明：
- 輸入格式：每一行一個正整數 N，遇到 0 表示結束（不處理 0）。
- 輸出格式：對於每個 N，輸出所有 1 ≤ i < j ≤ N 的 gcd(i, j) 總和。

實作說明（繁體中文註解）：
- 由於 N 的上限為 500，使用雙層迴圈暴力計算是可接受且最容易理解的做法。
- 程式流程：逐行讀取 N（遇到 0 中斷），對每個 N 使用生成式累加所有 gcd 值，最後把結果一行行輸出。

這個檔案刻意保留最簡潔的寫法，方便記憶與複習演算法思想。
"""

from __future__ import annotations

from math import gcd
import sys


def solve() -> None:
    """主程式入口。

    逐行讀取標準輸入，對每個 N 計算所需的 G 值，遇到 0 則結束讀取。
    計算時採用暴力法：對所有 i<j 計算 gcd(i,j) 並加總。
    """

    answers: list[str] = []

    # 讀取每一行並轉成整數 N
    for line in sys.stdin:
        n = int(line)
        if n == 0:  # 根據題目規範，0 為結束標記
            break

        # 使用生成式(sum)與內建 gcd 加總，表達簡潔且易於閱讀
        total = sum(gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        answers.append(str(total))

    # 一次性輸出所有結果，每個結果換行
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()
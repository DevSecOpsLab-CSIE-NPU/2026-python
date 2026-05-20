"""
cheapest_base-easy.py

簡化且易記的 UVA 11005 解法範例，重點註解為繁體中文，說明每個步驟的目的與實作要點。

使用情境：作為筆記或比對原始解法時的參考版，保留直覺易懂的函式與資料流。

功能要點：
- `cost_in_base(n, b, costs)`：用除餘法計算 n 在進位 b 時的總印刷成本。
- `best_bases(costs, n)`：在 2..36 中找出成本最小的所有進位。
- `main()`：簡單將 stdin token 化後依序解析（符合題目輸入格式），並輸出結果。

註：此檔案以可讀性為目的，非最極端微優化版本；時間複雜度對題目輸入大小是足夠的。
"""

import sys
from typing import List


def cost_in_base(n: int, b: int, costs: List[int]) -> int:
    """回傳整數 n 在進位 b 下的印刷總成本。

    實作細節：使用除餘法 (n % b, n //= b) 把數字拆成各位。每個位元值當作 costs 的索引。
    - 若 n == 0，代表表示為單一字元 '0'，成本為 costs[0]。
    - 回傳值為整數總成本。
    """
    # 特殊情況：0 的表示只有一個字元 '0'
    if n == 0:
        return costs[0]

    total = 0
    x = n
    # 從低位到高位累加成本
    while x > 0:
        digit = x % b  # 取得最低位的數值 (0..b-1)
        total += costs[digit]
        x //= b
    return total


def best_bases(costs: List[int], n: int) -> List[int]:
    """找出所有使總成本最小的進位（2..36），以升序回傳。

    實作說明：
    - 先對每個 b 計算成本，並把 (cost, b) 收集起來。
    - 排序後第一個元素為最小成本；再取出所有成本等於該最小值的進位。
    - 此方法直觀且易記；也可以改用一次掃描維護最小值以節省排序開銷。
    """
    vals = [(cost_in_base(n, b, costs), b) for b in range(2, 37)]
    vals.sort()  # 依 cost 先排序，再依 base（數字）排序
    min_cost = vals[0][0]
    # 取出所有成本等於 min_cost 的進位
    return [b for c, b in vals if c == min_cost]


def main():
    """主程式：從 stdin 讀取所有 token 並依題目格式解析輸入。

    輸入格式要點：
    - 第一個整數為測資組數 t。
    - 每組先有 36 個成本值（分 4 行輸入，但在 token 化後連續出現）。
    - 接著一個整數 q 為查詢數量，接著 q 個十進位整數查詢值。

    為簡潔起見，採用一個指標 p 遍歷 token 陣列（類似手寫的 iterator）。
    """
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    p = 0
    t = int(tokens[p]); p += 1

    out_lines: List[str] = []
    for case in range(1, t + 1):
        # 讀取 36 個成本值，順序對應 '0'..'9','A'..'Z'
        costs = list(map(int, tokens[p:p + 36])); p += 36

        q = int(tokens[p]); p += 1
        out_lines.append(f"Case {case}:")
        for _ in range(q):
            n = int(tokens[p]); p += 1
            bs = best_bases(costs, n)
            out_lines.append(f"Cheapest base(s) for number {n}: {' '.join(map(str, bs))}")

        # 題目要求測資之間空一行
        if case != t:
            out_lines.append("")

    # 一次輸出所有行，避免多次 flush
    print('\n'.join(out_lines))


if __name__ == '__main__':
    main()

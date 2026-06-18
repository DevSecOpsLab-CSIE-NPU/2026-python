"""
UVA 11005 — Cheapest Base 解題輔助模組

此模組實作 `cheapest_bases(costs, N)` 函式，回傳在 2..36 進位中
表示 N 時成本最低的進位列表。

註解說明：
- 算法：對每個進位 b (2..36)，將 N 轉成 base-b 的各位數字，
  並將各位數字對應的成本相加得到該進位的總成本。
- 若 N==0，則表示為單一位元 '0'，成本為 costs[0]。
- 最後回傳所有達到最小總成本的進位（升序）。

時間複雜度：對每個進位 b，對 N 做除法取餘的位數次數約為 O(log_b N)，
因此最壞情況總和約 O(sum_b log_b N)；在本題常數範圍 (b=2..36)，
實際上運算量很小且可接受。

空間複雜度：O(1)（除了用於暫存結果的常數大小列表）。
"""

from typing import List


def cheapest_bases(costs: List[int], N: int) -> List[int]:
    """
    計算在不同進位（2..36）下印刷數字 N 的總成本，回傳成本最小的進位列表（升序）。

    參數：
    - costs: 長度 36 的整數列表，對應數字 0..35 的字元成本。
    - N: 非負整數（0 <= N <= 2,000,000,000）。

    回傳：
    - 一個整數列表，包含所有成本最低的進位（例如 [2, 5, 10]）。
    """
    if len(costs) != 36:
        # 防禦式檢查：確保 costs 有 36 個元素
        raise ValueError("costs must have length 36")

    results = []  # 儲存 (總成本, 進位) 的列表
    for base in range(2, 37):
        if N == 0:
            # N==0 在任何進位下均為單一位 '0'
            total = costs[0]
        else:
            total = 0
            x = N
            # 將 N 轉換為 base 進位的各個數字，累加對應的成本
            while x > 0:
                digit = x % base
                total += costs[digit]
                x //= base
        results.append((total, base))

    # 找出最低成本，然後回傳所有達到此成本的進位（升序）
    min_cost = min(c for c, b in results)
    best = [b for c, b in results if c == min_cost]
    return best


__all__ = ["cheapest_bases"]

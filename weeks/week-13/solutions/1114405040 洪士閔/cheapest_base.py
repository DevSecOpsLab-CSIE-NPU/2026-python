"""
UVA 11005 - Cheapest Base 的解題輔助函式。
包含：
- `cost_in_base(n, base, costs)`: 計算數字 n 在 base 進位下的印刷成本。
- `cheapest_bases(costs, n)`: 回傳成本最小的所有進位制 (2~36) 的清單。

註：此檔案僅提供函式以供 unit test 匯入與測試。
繁體中文註解以利教學與閱讀。
"""

from typing import List


def cost_in_base(n: int, base: int, costs: List[int]) -> int:
    """計算十進位整數 `n` 在 `base` 進位下的字元印刷總成本。

    參數:
    - n: 被查詢的十進位整數 (n >= 0)
    - base: 進位制 (2..36)
    - costs: 長度為 36 的整數陣列，對應字元 '0'..'9','A'..'Z' 的印刷成本

    回傳值:
    - 整數，表示總成本
    
    實作說明：使用除餘法（mod/div）分解 n 的每一位，對應的 digit 則當作 costs 的索引。
    若 n==0，表示只有單一字元 '0'，直接回傳 costs[0]。
    """
    # 處理 n == 0 的特殊情況
    if n == 0:
        return costs[0]

    total = 0
    value = n
    # 逐位取餘並累加對應成本
    while value > 0:
        digit = value % base
        total += costs[digit]
        value //= base

    return total


def cheapest_bases(costs: List[int], n: int) -> List[int]:
    """找出使數字 n 印刷成本最低的所有進位制 (2..36)。

    參數:
    - costs: 長度 36 的整數列表，依序對應 '0'..'9','A'..'Z'
    - n: 查詢的十進位非負整數

    回傳值:
    - 以升序排列的進位制列表，例如 [2,3,10]
    """
    if len(costs) != 36:
        raise ValueError("costs 長度必須為 36")

    results = []
    min_cost = None

    # 逐一檢查每個進位 (2..36)，計算成本並比較最小值
    for base in range(2, 37):
        c = cost_in_base(n, base, costs)
        if min_cost is None or c < min_cost:
            min_cost = c
            results = [base]
        elif c == min_cost:
            results.append(base)

    return results


if __name__ == "__main__":
    # 範例執行（僅示範函式使用）
    sample_costs = [1] * 36
    print(cheapest_bases(sample_costs, 0))

"""
題目 11005: Cheapest Base (簡易版 - Easy)
根據字元印刷成本，找出表示數字成本最低的進制

本版本採用詳細的中文註解説明每個步驟
"""


def to_base(n, base):
    """
    將十進位數字轉換到指定進制
    例如: to_base(100, 16) -> '64' (16進制)
    """
    # 定義進制使用的字元: 0-9 和 A-Z
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 邊界情況：如果數字是 0，直接返回 '0'
    if n == 0:
        return '0'

    result = []

    # 逐位計算進制表示
    while n > 0:
        remainder = n % base  # 獲得個位數字
        result.append(digits[remainder])  # 轉換為對應的字元
        n = n // base  # 去掉個位

    # 由於是從低位到高位計算，需要反轉
    return ''.join(reversed(result))


def calculate_cost(representation, costs):
    """
    計算進制表示的總成本
    例如: representation='64', costs=..., 則計算 costs[6] + costs[4]
    """
    total = 0

    # 遍歷每個字元
    for ch in representation:
        if ch.isdigit():
            # 數字 0-9 對應 costs[0-9]
            total += costs[int(ch)]
        else:
            # 字母 A-Z 對應 costs[10-35]
            # ord('A') = 65, 所以 ord('A')-ord('A')+10 = 10
            total += costs[ord(ch) - ord('A') + 10]

    return total


def find_cheapest_bases(num, costs):
    """
    找出表示數字成本最低的進制

    步驟：
    1. 將數字轉換到所有進制 (2-36)
    2. 計算每個進制下的成本
    3. 找出最低成本
    4. 收集所有成本最低的進制，升序排列
    """
    base_costs = []

    # 嘗試所有進制 2 到 36
    for base in range(2, 37):
        # 轉換到該進制
        rep = to_base(num, base)

        # 計算成本
        cost = calculate_cost(rep, costs)

        # 記錄 (成本, 進制) 對
        base_costs.append((cost, base))

    # 找出最低成本
    min_cost = min(base_costs, key=lambda x: x[0])[0]

    # 收集所有成本為最低的進制
    best_bases = []
    for cost, base in base_costs:
        if cost == min_cost:
            best_bases.append(base)

    # 升序排列並返回
    return sorted(best_bases)


def solve(costs=None, num=None):
    """
    主求解函數
    接收進制成本列表和查詢數字，返回最便宜進制的列表
    """
    if costs is None or num is None:
        return []

    return find_cheapest_bases(num, costs)

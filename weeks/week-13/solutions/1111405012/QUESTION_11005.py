"""
題目 11005: Cheapest Base (正式版)
根據字元印刷成本，找出表示數字成本最低的進制

核心演算法：
1. 將十進位數字轉換到各進制 (2-36)
2. 計算每個進制下表示的成本
3. 找出成本最低的進制（可能多個）
"""

from typing import List, Tuple


def to_base(n: int, base: int) -> str:
    """
    將十進位數字轉換到指定進制

    Args:
        n: 十進位正整數
        base: 目標進制 (2-36)

    Returns:
        該進制下的表示 (use 0-9, A-Z)
    """
    if n == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    while n > 0:
        result.append(digits[n % base])
        n //= base

    return ''.join(reversed(result))


def calculate_cost(representation: str, costs: List[int]) -> int:
    """
    計算進制表示的總成本

    Args:
        representation: 進制表示字串 (0-9, A-Z)
        costs: 36個字元的成本陣列 (0-9 對應 costs[0-9], A-Z 對應 costs[10-35])

    Returns:
        該表示的總成本
    """
    total = 0
    for ch in representation:
        if ch.isdigit():
            total += costs[int(ch)]
        else:
            total += costs[ord(ch) - ord('A') + 10]
    return total


def find_cheapest_bases(num: int, costs: List[int]) -> List[int]:
    """
    找出表示數字成本最低的進制

    Args:
        num: 查詢的十進位數字
        costs: 36個字元的成本陣列

    Returns:
        成本最低的進制列表 (升序)
    """
    base_costs = []

    for base in range(2, 37):
        rep = to_base(num, base)
        cost = calculate_cost(rep, costs)
        base_costs.append((cost, base))

    # 找最低成本
    min_cost = min(base_costs, key=lambda x: x[0])[0]

    # 收集所有成本最低的進制
    best_bases = [base for cost, base in base_costs if cost == min_cost]

    return sorted(best_bases)


def solve(costs: List[int] = None, num: int = None) -> List[int]:
    """
    主求解函數

    Args:
        costs: 36個字元的成本陣列
        num: 查詢的十進位數字

    Returns:
        成本最低的進制列表
    """
    if costs is None or num is None:
        return []

    return find_cheapest_bases(num, costs)

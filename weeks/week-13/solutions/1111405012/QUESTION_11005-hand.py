"""
題目 11005: Cheapest Base (簡化版 - SU)
"""


def to_base(n, base):
    if n == 0:
        return '0'
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while n > 0:
        result.append(digits[n % base])
        n //= base
    return ''.join(reversed(result))


def calculate_cost(representation, costs):
    total = 0
    for ch in representation:
        idx = int(ch) if ch.isdigit() else ord(ch) - ord('A') + 10
        total += costs[idx]
    return total


def find_cheapest_bases(num, costs):
    base_costs = [(calculate_cost(to_base(num, b), costs), b)
                  for b in range(2, 37)]
    min_cost = min(base_costs)[0]
    return sorted([b for c, b in base_costs if c == min_cost])


def solve(costs=None, num=None):
    return find_cheapest_bases(num, costs) if costs and num is not None else []

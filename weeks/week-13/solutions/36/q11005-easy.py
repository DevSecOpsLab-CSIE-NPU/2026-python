from typing import List


def cost_in_base(n: int, base: int, costs: List[int]) -> int:
    """用最直觀的方式計算 n 在 base 的成本。"""
    if n == 0:
        return costs[0]
    total = 0
    current = n
    while current > 0:
        digit = current % base
        total += costs[digit]
        current //= base
    return total


def cheapest_bases(costs: List[int], n: int) -> List[int]:
    """直接逐一檢查 2~36 進位，找出最小成本的進位制。"""
    best_cost = None
    best_bases: List[int] = []
    for base in range(2, 37):
        cost = cost_in_base(n, base, costs)
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_bases = [base]
        elif cost == best_cost:
            best_bases.append(base)
    return best_bases


def solve(lines: List[str]) -> List[str]:
    """使用容易記憶的解析方式處理輸入。"""
    lines = [line.strip() for line in lines if line.strip() != ""]
    index = 0
    t = int(lines[index])
    index += 1
    output: List[str] = []

    for case in range(1, t + 1):
        cost_values: List[int] = []
        for _ in range(4):
            row = lines[index]
            index += 1
            cost_values.extend(int(x) for x in row.split())
        q = int(lines[index])
        index += 1

        output.append(f"Case {case}:")
        for _ in range(q):
            n = int(lines[index])
            index += 1
            bases = cheapest_bases(cost_values, n)
            output.append(f"Cheapest base(s) for number {n}: {' '.join(str(b) for b in bases)}")
        if case != t:
            output.append("")

    return output


def main() -> None:
    import sys
    data = [line.rstrip("\n") for line in sys.stdin]
    result = solve(data)
    print("\n".join(result))


if __name__ == "__main__":
    main()

from typing import List


def parse_costs(lines: List[str]) -> List[int]:
    """解析 4 行成本資料，回傳 36 個字元成本。"""
    values: List[int] = []
    for line in lines:
        values.extend(int(x) for x in line.split())
    if len(values) != 36:
        raise ValueError("成本資料必須有 36 個整數")
    return values


def cost_in_base(n: int, base: int, costs: List[int]) -> int:
    """計算數字 n 以 base 進位表示時的總印刷成本。"""
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total


def cheapest_bases(costs: List[int], n: int) -> List[int]:
    """找出最便宜的進位制，並以升序回傳所有最小成本的進位。"""
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


def format_answer(n: int, bases: List[int]) -> str:
    """格式化輸出字串。"""
    return f"Cheapest base(s) for number {n}: {' '.join(str(b) for b in bases)}"


def solve(lines: List[str]) -> List[str]:
    """處理整個輸入，回傳每一行要輸出的結果。"""
    it = iter(line.strip() for line in lines if line.strip() != "")
    t = int(next(it))
    result: List[str] = []
    for case in range(1, t + 1):
        cost_lines = [next(it) for _ in range(4)]
        costs = parse_costs(cost_lines)
        q = int(next(it))
        result.append(f"Case {case}:")
        for _ in range(q):
            n = int(next(it))
            best_bases = cheapest_bases(costs, n)
            result.append(format_answer(n, best_bases))
        if case != t:
            result.append("")
    return result


def main() -> None:
    import sys

    lines = [line.rstrip("\n") for line in sys.stdin]
    output_lines = solve(lines)
    print("\n".join(output_lines))


if __name__ == "__main__":
    main()

"""UVA 100 - 3n + 1（簡單版）"""

import sys


memo = {1: 1}


def cycle_length(n: int) -> int:
    """回傳 n 的 cycle length（包含起點與 1）。"""
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        memo[n] = 1 + cycle_length(n // 2)
    else:
        memo[n] = 1 + cycle_length(3 * n + 1)
    return memo[n]


def solve(data: str) -> str:
    outputs = []
    for line in data.strip().splitlines():
        if not line.strip():
            continue
        i, j = map(int, line.split())
        left, right = min(i, j), max(i, j)
        best = 0
        for n in range(left, right + 1):
            best = max(best, cycle_length(n))
        outputs.append(f"{i} {j} {best}")
    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

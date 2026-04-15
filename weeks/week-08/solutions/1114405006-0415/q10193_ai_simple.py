"""
UVA 10193
AI 教學簡單版本（含中文註解）
"""

import sys


def min_b_plus_c(a: int) -> int:
    # 由 arctan 恆等式可推得：(b-a)(c-a) = a^2 + 1
    n = a * a + 1

    # 固定乘積時，兩因數越接近，和越小
    # 掃到 sqrt(n) 找最大的可整除因數 d
    d = 1
    i = 1
    while i * i <= n:
        if n % i == 0:
            d = i
        i += 1

    x = d
    y = n // d

    # b = a + x, c = a + y
    return (a + x) + (a + y)


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    out = []

    for a in nums:
        out.append(str(min_b_plus_c(a)))

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()

"""
UVA 10193 - Arctan Decomposition (course version)
簡單版（CPE 現場可手打）
"""


def min_b_plus_c(a: int) -> int:
    # 由 arctan 恆等式可推到：(b-a)(c-a) = a^2 + 1
    n = a * a + 1

    # 為了讓 b + c 最小，需要讓兩因數盡量接近
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


def solve() -> None:
    import sys

    nums = [int(x) for x in sys.stdin.read().split()]
    out = []

    for a in nums:
        out.append(str(min_b_plus_c(a)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

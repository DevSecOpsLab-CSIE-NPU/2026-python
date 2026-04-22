# UVA 10268 - 498-bis
# 詳細註解版（繁體中文）

import sys


def derivative_value_at_x(x: int, coeffs: list[int]) -> int:
    # 若多項式為常數，導數為 0
    n = len(coeffs) - 1
    if n <= 0:
        return 0

    # P(x) = a0*x^n + a1*x^(n-1) + ... + an
    # P'(x) = n*a0*x^(n-1) + (n-1)*a1*x^(n-2) + ... + a(n-1)
    # 使用 Horner 形式計算導數值，避免顯式冪次運算
    res = coeffs[0] * n
    degree = n - 1

    for i in range(1, n):
        res = res * x + coeffs[i] * degree
        degree -= 1

    return res


def solve() -> None:
    lines = [ln.strip() for ln in sys.stdin if ln.strip() != ""]
    out = []

    # 每組資料 2 行：
    # 第 1 行 x
    # 第 2 行係數（由最高次到常數項）
    i = 0
    while i + 1 < len(lines):
        x = int(lines[i])
        coeffs = list(map(int, lines[i + 1].split()))
        i += 2

        out.append(str(derivative_value_at_x(x, coeffs)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

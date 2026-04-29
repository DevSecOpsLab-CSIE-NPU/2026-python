import sys

def derivative_value_at_x(x, coeffs):
    n = len(coeffs) - 1
    if n <= 0:
        return 0

    res = coeffs[0] * n
    degree = n - 1

    for i in range(1, n):
        res = res * x + coeffs[i] * degree
        degree -= 1

    return res

def solve():
    lines = [ln.strip() for ln in sys.stdin if ln.strip() != ""]
    out = []

    i = 0
    while i + 1 < len(lines):
        x = int(lines[i])
        coeffs = list(map(int, lines[i + 1].split()))
        i += 2

        out.append(str(derivative_value_at_x(x, coeffs)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
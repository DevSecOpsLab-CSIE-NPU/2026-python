import sys


def win_probability(n: int, p: float, i: int) -> float:
    if p == 0.0:
        return 0.0

    q = 1.0 - p
    numerator = (q ** (i - 1)) * p
    denominator = 1.0 - (q ** n)

    if denominator == 0.0:
        return 0.0

    return numerator / denominator


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    s = int(parts[0])
    idx = 1
    ans = []

    for _ in range(s):
        n = int(parts[idx])
        p = float(parts[idx + 1])
        i = int(parts[idx + 2])
        idx += 3
        ans.append(f"{win_probability(n, p, i):.4f}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

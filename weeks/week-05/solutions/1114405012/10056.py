import sys


def win_probability(n: int, p: float, i: int) -> float:
    """計算第 i 位玩家最終獲勝機率。"""
    if p == 0.0:
        return 0.0

    q = 1.0 - p
    numerator = (q ** (i - 1)) * p
    denominator = 1.0 - (q ** n)

    if denominator == 0.0:
        return 0.0

    return numerator / denominator


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    s = int(tokens[0])
    idx = 1
    answers = []

    for _ in range(s):
        n = int(tokens[idx])
        p = float(tokens[idx + 1])
        i = int(tokens[idx + 2])
        idx += 3

        ans = win_probability(n, p, i)
        answers.append(f"{ans:.4f}")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))

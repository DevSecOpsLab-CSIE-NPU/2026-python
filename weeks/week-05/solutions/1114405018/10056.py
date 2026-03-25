from typing import List, Tuple


def win_probability(n: int, p: float, i: int) -> float:
    """回傳第 i 位玩家最終獲勝機率。"""
    if p == 0.0:
        return 0.0

    q = 1.0 - p
    numerator = p * (q ** (i - 1))
    denominator = 1.0 - (q ** n)
    return numerator / denominator


def solve(data: str) -> str:
    """解析輸入並輸出每組答案（四位小數）。"""
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    out: List[str] = []

    for _ in range(t):
        n = int(tokens[idx])
        p = float(tokens[idx + 1])
        i = int(tokens[idx + 2])
        idx += 3

        prob = win_probability(n, p, i)
        out.append(f"{prob:.4f}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))

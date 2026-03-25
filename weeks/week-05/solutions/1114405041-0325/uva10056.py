"""UVA 10056 - What is the Probability ?（主解法）。

機率模型：
- 每位玩家輪流嘗試成功機率 p。
- 若有人成功，該局結束。
- 問第 i 位玩家最終贏的機率。

公式：
P(i) = p * (1-p)^(i-1) / (1 - (1-p)^n)
當 p = 0 時，機率為 0。
"""

from __future__ import annotations


def winning_probability(n: int, p: float, i: int) -> float:
    """計算第 i 位玩家勝出的機率。"""
    if p == 0.0:
        return 0.0

    q = 1.0 - p
    denominator = 1.0 - (q ** n)
    if denominator == 0.0:
        return 0.0

    numerator = p * (q ** (i - 1))
    return numerator / denominator


def solve_io(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    outputs: list[str] = []

    for _ in range(t):
        n = int(tokens[idx])
        p = float(tokens[idx + 1])
        i = int(tokens[idx + 2])
        idx += 3

        outputs.append(f"{winning_probability(n, p, i):.4f}")

    return "\n".join(outputs)


def main() -> None:
    import sys

    print(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()

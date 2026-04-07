import sys
from typing import List


def player_win_probability(n: int, p: float, i: int) -> float:
    if p <= 0:
        return 0.0
    q = 1.0 - p
    numerator = p * (q ** (i - 1))
    denominator = 1.0 - (q ** n)
    return numerator / denominator if denominator != 0 else 0.0


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    results: List[str] = []
    for _ in range(t):
        n = int(next(it))
        p = float(next(it))
        i = int(next(it))
        prob = player_win_probability(n, p, i)
        results.append(f"{prob:.4f}")

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()

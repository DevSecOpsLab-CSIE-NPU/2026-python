"""
UVA 10056 - What is the Probability?
"""

from __future__ import annotations


def winning_probability(player_count: int, success_probability: float, player_index: int) -> float:
    """計算第 player_index 位玩家最後獲勝的機率。"""
    if success_probability == 0:
        return 0.0

    fail_probability = 1 - success_probability
    return (
        (fail_probability ** (player_index - 1)) * success_probability
        / (1 - fail_probability**player_count)
    )


def solve(text: str) -> str:
    """依題目格式輸出每筆機率，保留四位小數。"""
    tokens = text.split()
    if not tokens:
        return ""

    case_count = int(tokens[0])
    index = 1
    results: list[str] = []

    for _ in range(case_count):
        player_count = int(tokens[index])
        success_probability = float(tokens[index + 1])
        player_index = int(tokens[index + 2])
        index += 3
        results.append(f"{winning_probability(player_count, success_probability, player_index):.4f}")

    return "\n".join(results)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

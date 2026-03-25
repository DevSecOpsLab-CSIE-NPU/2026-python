from __future__ import annotations

import sys


def winning_probability(player_count: int, success_probability: float, target_player: int) -> float:
    # 若每次都不可能成功，任何玩家都不可能贏。
    if success_probability == 0.0:
        return 0.0

    failure_probability = 1.0 - success_probability
    full_round_failure_probability = failure_probability ** player_count

    # 第 i 位玩家要獲勝，代表前面 i - 1 位都失敗，接著自己成功。
    current_round_success = (failure_probability ** (target_player - 1)) * success_probability

    # 若前面整輪都沒人成功，遊戲就會重複，因此形成等比級數。
    return current_round_success / (1.0 - full_round_failure_probability)


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    test_case_count = int(tokens[0])
    index = 1
    answers: list[str] = []

    for _ in range(test_case_count):
        player_count = int(tokens[index])
        success_probability = float(tokens[index + 1])
        target_player = int(tokens[index + 2])
        index += 3

        probability = winning_probability(player_count, success_probability, target_player)
        answers.append(f"{probability:.4f}")

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
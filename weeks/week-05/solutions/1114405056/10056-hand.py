from __future__ import annotations

import sys


def winning_probability(player_count: int, success_probability: float, target_player: int) -> float:
    # If a single attempt can never succeed, no player can ever win.
    if success_probability == 0.0:
        return 0.0

    # q is the probability of failing on one turn.
    failure_probability = 1.0 - success_probability

    # Probability that the target player wins in the current round:
    # everyone before them fails, then they succeed.
    current_round_success = (failure_probability ** (target_player - 1)) * success_probability

    # Probability that all players fail in one full round.
    full_round_failure_probability = failure_probability ** player_count

    # If nobody wins in the first round, the game repeats.
    # This creates a geometric series with ratio full_round_failure_probability.
    return current_round_success / (1.0 - full_round_failure_probability)


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    index = 1
    outputs: list[str] = []

    for _ in range(case_count):
        player_count = int(parts[index])
        success_probability = float(parts[index + 1])
        target_player = int(parts[index + 2])
        index += 3

        answer = winning_probability(player_count, success_probability, target_player)
        outputs.append(f"{answer:.4f}")

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
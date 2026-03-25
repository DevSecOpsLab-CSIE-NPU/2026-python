from __future__ import annotations

import sys


def winning_probability(player_count: int, success_probability: float, target_player: int) -> float:
    # 如果一次成功的機率就是 0，代表遊戲永遠不會結束，
    # 所以指定玩家的獲勝機率自然也是 0。
    if success_probability == 0.0:
        return 0.0

    # q 代表一次失敗的機率。
    failure_probability = 1.0 - success_probability

    # 指定玩家在「目前這一輪」獲勝的機率：
    # 前面的人都失敗，輪到自己時成功。
    current_round_success = (failure_probability ** (target_player - 1)) * success_probability

    # 一整輪 N 個玩家都失敗的機率。
    full_round_failure_probability = failure_probability ** player_count

    # 如果第一輪沒人成功，遊戲就會進入第二輪；
    # 第二輪沒人成功，又會進入第三輪。
    # 因此總機率是：
    # current_round_success * (1 + r + r^2 + ...)
    # 其中 r = full_round_failure_probability
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
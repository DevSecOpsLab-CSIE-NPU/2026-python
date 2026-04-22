from __future__ import annotations

import sys


def solve_case(eggs: int, floors: int) -> str:
    # 用反向 DP：已知丟 t 次、用 k 顆蛋，最多能確認幾層樓。
    if floors == 0:
        return "0"

    reach = [0] * (eggs + 1)
    for trials in range(1, 64):
        for egg_count in range(eggs, 0, -1):
            reach[egg_count] = reach[egg_count] + reach[egg_count - 1] + 1
        if reach[eggs] >= floors:
            return str(trials)
    return "More than 63 trials needed."


def main() -> None:
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    outputs: list[str] = []
    index = 0
    while index + 1 < len(tokens):
        eggs = tokens[index]
        floors = tokens[index + 1]
        index += 2
        if eggs == 0:
            break
        outputs.append(solve_case(eggs, floors))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
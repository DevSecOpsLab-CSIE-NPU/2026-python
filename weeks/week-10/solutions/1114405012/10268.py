from __future__ import annotations

import sys


def solve_case(eggs: int, floors: int) -> str:
    # 0 層樓不需測試。
    if floors == 0:
        return "0"

    # reach[k] 代表目前試驗次數下，k 顆蛋最多可判定幾層樓。
    reach = [0] * (eggs + 1)
    for trials in range(1, 64):
        # 反向更新避免同一輪覆蓋到舊值。
        for egg_count in range(eggs, 0, -1):
            reach[egg_count] = reach[egg_count] + reach[egg_count - 1] + 1
        if reach[eggs] >= floors:
            return str(trials)

    # 題目要求超過 63 次就輸出固定字串。
    return "More than 63 trials needed."


def main() -> None:
    # 多筆 k, n，遇到 k=0 結束。
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
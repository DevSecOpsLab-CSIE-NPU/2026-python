from __future__ import annotations

from typing import Iterable


def is_consistent(
    coin: int,
    assume_heavier: bool,
    weighings: Iterable[tuple[list[int], list[int], str]],
) -> bool:
    for left, right, result in weighings:
        in_left = coin in left
        in_right = coin in right

        # 如果秤重平衡，代表這次拿去秤的硬幣一定都是真的。
        if result == "=":
            if in_left or in_right:
                return False
            continue

        # 假設這顆硬幣比較重或比較輕，檢查是否符合本次秤重結果。
        if assume_heavier:
            if result == "<" and not in_right:
                return False
            if result == ">" and not in_left:
                return False
        else:
            if result == "<" and not in_left:
                return False
            if result == ">" and not in_right:
                return False

        # 若天平不平衡，但候選硬幣根本沒上秤，就不可能造成這次結果。
        if not in_left and not in_right:
            return False

    return True


def find_fake_coin(
    coin_count: int, weighings: list[tuple[list[int], list[int], str]]
) -> int:
    possible_coins: list[int] = []

    # 逐一測試每顆硬幣是否可能是假幣，並同時考慮偏重或偏輕。
    for coin in range(1, coin_count + 1):
        heavier_ok = is_consistent(coin, True, weighings)
        lighter_ok = is_consistent(coin, False, weighings)
        if heavier_ok or lighter_ok:
            possible_coins.append(coin)

    if len(possible_coins) == 1:
        return possible_coins[0]
    return 0


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines()]
    index = 0

    # 輸入格式允許空白行，先跳過開頭空行。
    while index < len(lines) and lines[index] == "":
        index += 1

    test_case_count = int(lines[index])
    index += 1
    answers: list[str] = []

    for _ in range(test_case_count):
        while index < len(lines) and lines[index] == "":
            index += 1

        coin_count, weigh_count = map(int, lines[index].split())
        index += 1

        weighings: list[tuple[list[int], list[int], str]] = []
        for _ in range(weigh_count):
            # 每次秤重先讀左右兩邊硬幣編號，再讀下一行的比較結果。
            parts = list(map(int, lines[index].split()))
            index += 1
            count_per_side = parts[0]
            left = parts[1 : 1 + count_per_side]
            right = parts[1 + count_per_side : 1 + count_per_side * 2]
            result = lines[index]
            index += 1
            weighings.append((left, right, result))

        answers.append(str(find_fake_coin(coin_count, weighings)))

    return "\n\n".join(answers)


def main() -> None:
    import sys

    # 直接讀取標準輸入並輸出答案，符合線上評測需求。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
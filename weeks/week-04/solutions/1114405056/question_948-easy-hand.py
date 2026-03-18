"""HAND EASY - QUESTION 948"""

from __future__ import annotations

import sys


def read_cases(text: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    lines = text.splitlines()
    index = 0

    while index < len(lines) and not lines[index].strip():
        index += 1

    if index == len(lines):
        return []

    case_count = int(lines[index].strip())
    index += 1
    cases = []

    for _ in range(case_count):
        while index < len(lines) and not lines[index].strip():
            index += 1

        coin_count, weigh_count = map(int, lines[index].split())
        index += 1
        weighings = []

        for _ in range(weigh_count):
            while index < len(lines) and not lines[index].strip():
                index += 1

            numbers = list(map(int, lines[index].split()))
            index += 1

            while index < len(lines) and not lines[index].strip():
                index += 1

            result = lines[index].strip()
            index += 1

            size = numbers[0]
            left = numbers[1 : 1 + size]
            right = numbers[1 + size : 1 + 2 * size]
            weighings.append((left, right, result))

        cases.append((coin_count, weighings))

    return cases


def matches_all_weighings(coin: int, heavier: bool, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in weighings:
        delta = 0

        if coin in left:
            delta += 1 if heavier else -1
        if coin in right:
            delta -= 1 if heavier else -1

        if delta > 0 and result != ">":
            return False
        if delta < 0 and result != "<":
            return False
        if delta == 0 and result != "=":
            return False

    return True


def solve(text: str) -> str:
    outputs = []

    for coin_count, weighings in read_cases(text):
        possible_coins = []

        for coin in range(1, coin_count + 1):
            if matches_all_weighings(coin, True, weighings) or matches_all_weighings(coin, False, weighings):
                possible_coins.append(coin)

        outputs.append(str(possible_coins[0]) if len(possible_coins) == 1 else "0")

    return "\n\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

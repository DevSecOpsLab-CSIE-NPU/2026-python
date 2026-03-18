"""QUESTION-948 easy 版。

這版刻意用最直接的暴力枚舉方式來寫：
1. 先假設第 1 枚硬幣是假的，而且它比較重。
2. 再假設第 1 枚硬幣是假的，而且它比較輕。
3. 依序把所有硬幣都這樣試一次。
4. 只要該假設和全部秤重結果都吻合，就把這枚硬幣記下來。

因為最多只有 100 枚硬幣、100 次秤重，
這種寫法雖然不是最花俏，但非常穩定，也很好記憶。
"""

from __future__ import annotations

import sys


def read_cases(text: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    """把輸入拆成多組測資，方便後續逐題判斷。"""

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
    """檢查「某枚硬幣 + 某種重量方向」是否能解釋全部秤重結果。"""

    for left, right, result in weighings:
        # delta > 0 代表左邊比較重，delta < 0 代表左邊比較輕。
        delta = 0

        if coin in left:
            if heavier:
                delta += 1
            else:
                delta -= 1

        if coin in right:
            if heavier:
                delta -= 1
            else:
                delta += 1

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

        if len(possible_coins) == 1:
            outputs.append(str(possible_coins[0]))
        else:
            outputs.append("0")

    return "\n\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

"""QUESTION-948 正式版解答。

依照題目內容，這題實際上是天平假幣判定問題。
做法是枚舉每一枚硬幣，分別假設它比較重或比較輕，
只要某個假設能和所有秤重結果一致，就保留為候選答案。
最後若只有唯一一枚硬幣仍然可能是假幣，就輸出它的編號；
否則輸出 0。
"""

from __future__ import annotations

import sys


def parse_cases(text: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    lines = iter(text.splitlines())

    first_line = ""
    for line in lines:
        if line.strip():
            first_line = line.strip()
            break

    if not first_line:
        return []

    case_count = int(first_line)
    cases = []

    for _ in range(case_count):
        header = ""
        for line in lines:
            if line.strip():
                header = line.strip()
                break

        if not header:
            break

        coin_count, weigh_count = map(int, header.split())
        weighings = []

        for _ in range(weigh_count):
            data_line = ""
            for line in lines:
                if line.strip():
                    data_line = line.strip()
                    break

            result_line = ""
            for line in lines:
                if line.strip():
                    result_line = line.strip()
                    break

            numbers = list(map(int, data_line.split()))
            size = numbers[0]
            left = numbers[1 : 1 + size]
            right = numbers[1 + size : 1 + 2 * size]
            weighings.append((left, right, result_line))

        cases.append((coin_count, weighings))

    return cases


def is_consistent(coin: int, is_heavy: bool, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in weighings:
        delta = 0

        if coin in left:
            delta += 1 if is_heavy else -1
        if coin in right:
            delta -= 1 if is_heavy else -1

        predicted = "="
        if delta > 0:
            predicted = ">"
        elif delta < 0:
            predicted = "<"

        if predicted != result:
            return False

    return True


def find_false_coin(coin_count: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    candidates = []

    for coin in range(1, coin_count + 1):
        # 同一枚硬幣只要有一種重量方向能成立，就先保留為候選者。
        if is_consistent(coin, True, weighings) or is_consistent(coin, False, weighings):
            candidates.append(coin)

    return candidates[0] if len(candidates) == 1 else 0


def solve(text: str) -> str:
    answers = []
    for coin_count, weighings in parse_cases(text):
        # 每組測資之間需要輸出空白行，所以最後用雙換行串接。
        answers.append(str(find_false_coin(coin_count, weighings)))
    return "\n\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()

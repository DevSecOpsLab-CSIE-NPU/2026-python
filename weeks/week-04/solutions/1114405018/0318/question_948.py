"""UVA 948 - Find the Fake Coin

題意重點：
- 每筆測資只有一枚假幣，但不知道它是比較重還是比較輕。
- 透過多次天平秤重結果，找出唯一可能的假幣編號。
- 如果無法唯一判斷，就輸出 0。

解法概念：
- 逐一假設每一枚硬幣可能是「較重」或「較輕」的假幣。
- 檢查它是否能解釋所有秤重結果。
- 若最後只有一個硬幣編號符合，就輸出該編號；否則輸出 0。
"""

from __future__ import annotations

import sys


def parse_cases(data: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    """把輸入解析成多組測資。

    每組資料格式：
    - N K
    - 接下來 K 組秤重，每組兩行：
      1. Pi + 左邊 Pi 枚 + 右邊 Pi 枚
      2. 結果字元（<, >, =）
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return []

    case_count = int(lines[0])
    index = 1
    cases: list[tuple[int, list[tuple[list[int], list[int], str]]]] = []

    for _ in range(case_count):
        n_str, k_str = lines[index].split()
        index += 1
        n = int(n_str)
        k = int(k_str)

        weighings: list[tuple[list[int], list[int], str]] = []
        for _ in range(k):
            parts = list(map(int, lines[index].split()))
            index += 1
            result = lines[index]
            index += 1

            p = parts[0]
            left = parts[1 : 1 + p]
            right = parts[1 + p : 1 + 2 * p]
            weighings.append((left, right, result))

        cases.append((n, weighings))

    return cases


def matches(coin: int, heavier: bool, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    """檢查某枚硬幣在假設為較重/較輕時，是否能符合所有秤重結果。"""
    for left, right, result in weighings:
        if coin in left:
            expect = ">" if heavier else "<"
        elif coin in right:
            expect = "<" if heavier else ">"
        else:
            expect = "="

        if expect != result:
            return False

    return True


def solve(data: str) -> str:
    """依照題目格式輸出每筆測資的答案。"""
    cases = parse_cases(data)
    outputs: list[str] = []

    for n, weighings in cases:
        possible = set()

        for coin in range(1, n + 1):
            if matches(coin, True, weighings) or matches(coin, False, weighings):
                possible.add(coin)

        outputs.append(str(possible.pop()) if len(possible) == 1 else "0")

    return "\n\n".join(outputs)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()

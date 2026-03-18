from __future__ import annotations

import re
import sys


def _is_consistent(
    target_coin: int,
    is_heavier: bool,
    weighings: list[tuple[set[int], set[int], str]],
) -> bool:
    """檢查：假設 target_coin 是假幣，且是偏重/偏輕時，是否符合所有秤重結果。"""
    for left_coins, right_coins, result in weighings:
        # delta > 0 代表左盤比右盤重；delta < 0 代表左盤較輕；delta = 0 代表平衡
        delta = 0

        if target_coin in left_coins:
            delta += 1 if is_heavier else -1
        if target_coin in right_coins:
            delta += -1 if is_heavier else 1

        predicted = "="
        if delta > 0:
            predicted = ">"
        elif delta < 0:
            predicted = "<"

        if predicted != result:
            return False

    return True


def _find_fake_coin(n: int, weighings: list[tuple[set[int], set[int], str]]) -> int:
    """回傳唯一可行的假幣編號；若不唯一（或無解）則回傳 0。"""
    candidates: list[int] = []

    for coin in range(1, n + 1):
        heavier_ok = _is_consistent(coin, True, weighings)
        lighter_ok = _is_consistent(coin, False, weighings)

        if heavier_ok or lighter_ok:
            candidates.append(coin)

    return candidates[0] if len(candidates) == 1 else 0


def solve(data: str) -> str:
    """
    UVA 948（依題目敘述：找假幣）
    輸入可能包含空白行，因此使用 regex 抓取「數字」與「< > =」三種秤重符號。
    """
    tokens = re.findall(r"\d+|[<>=]", data)
    if not tokens:
        return ""

    idx = 0
    test_cases = int(tokens[idx])
    idx += 1

    answers: list[str] = []

    for _ in range(test_cases):
        if idx + 1 >= len(tokens):
            break

        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        weighings: list[tuple[set[int], set[int], str]] = []

        for _ in range(k):
            p = int(tokens[idx])
            idx += 1

            left = {int(tokens[idx + i]) for i in range(p)}
            idx += p

            right = {int(tokens[idx + i]) for i in range(p)}
            idx += p

            result = tokens[idx]
            idx += 1

            weighings.append((left, right, result))

        answers.append(str(_find_fake_coin(n, weighings)))

    # 題目要求每組測資之間空一行
    return "\n\n".join(answers)


def main() -> None:
    raw_input = sys.stdin.read()
    sys.stdout.write(solve(raw_input))


if __name__ == "__main__":
    main()

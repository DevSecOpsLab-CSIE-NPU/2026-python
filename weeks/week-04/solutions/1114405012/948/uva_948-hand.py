from __future__ import annotations

import re
import sys


def _check_assumption(
    coin: int,
    heavier: bool,
    weighings: list[tuple[set[int], set[int], str]],
) -> bool:
    """檢查某一個假設（某顆硬幣偏重或偏輕）是否符合全部秤重結果。"""
    for left_set, right_set, sign in weighings:
        # score > 0 代表左邊較重；score < 0 代表左邊較輕；score = 0 代表平衡
        score = 0

        if coin in left_set:
            score += 1 if heavier else -1
        if coin in right_set:
            score += -1 if heavier else 1

        if score > 0:
            predicted = ">"
        elif score < 0:
            predicted = "<"
        else:
            predicted = "="

        if predicted != sign:
            return False

    return True


def solve(data: str) -> str:
    """
    UVA 948 手打版

    做法：
    - 把輸入拆成數字與符號 token。
    - 對每一顆硬幣都嘗試「偏重」與「偏輕」兩種假設。
    - 能符合所有秤重結果的硬幣列為候選。
    - 候選只有一顆才輸出該編號，否則輸出 0。
    """
    tokens = re.findall(r"\d+|[<>=]", data)
    if not tokens:
        return ""

    idx = 0
    t = int(tokens[idx])
    idx += 1

    answers: list[str] = []

    for _ in range(t):
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        weighings: list[tuple[set[int], set[int], str]] = []

        for _ in range(k):
            p = int(tokens[idx])
            idx += 1

            left_set = {int(tokens[idx + i]) for i in range(p)}
            idx += p

            right_set = {int(tokens[idx + i]) for i in range(p)}
            idx += p

            sign = tokens[idx]
            idx += 1

            weighings.append((left_set, right_set, sign))

        possible: list[int] = []

        for coin in range(1, n + 1):
            if _check_assumption(coin, True, weighings) or _check_assumption(coin, False, weighings):
                possible.append(coin)

        answers.append(str(possible[0]) if len(possible) == 1 else "0")

    return "\n\n".join(answers)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()

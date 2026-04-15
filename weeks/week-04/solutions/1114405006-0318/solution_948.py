"""UVA 948 假幣問題解答。

解法核心：
1. 枚舉每一顆硬幣是否可能是假幣。
2. 對同一顆硬幣分別假設「比較重」與「比較輕」。
3. 逐筆模擬秤重，若與紀錄完全一致，該假設成立。
4. 最後若只有一顆硬幣仍可能是假幣，輸出其編號；否則輸出 0。
"""

from __future__ import annotations

import sys
from typing import Iterable


def _result_from_diff(diff: int) -> str:
    """把左右重量差轉回題目要求的符號。"""
    if diff < 0:
        return "<"
    if diff > 0:
        return ">"
    return "="


def _is_coin_consistent(
    coin: int,
    sign: int,
    weighings: Iterable[tuple[list[int], list[int], str]],
) -> bool:
    """
    檢查某顆硬幣在「較重或較輕」假設下，是否符合全部秤重紀錄。

    sign = +1 表示這顆假幣比較重。
    sign = -1 表示這顆假幣比較輕。
    """
    for left, right, expected in weighings:
        # diff 代表「左盤總重量 - 右盤總重量」在此假設下的相對差值。
        diff = 0
        if coin in left:
            diff += sign
        if coin in right:
            diff -= sign

        # 若任一筆秤重與紀錄不一致，代表此假設不可能成立。
        if _result_from_diff(diff) != expected:
            return False
    return True


def _find_fake_coin(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    """若可唯一確定假幣則回傳編號，否則回傳 0。"""
    possible: list[int] = []

    for coin in range(1, n + 1):
        # 只要「較重」或「較輕」其中一種成立，就代表此硬幣仍有可能是假幣。
        if _is_coin_consistent(coin, +1, weighings) or _is_coin_consistent(
            coin, -1, weighings
        ):
            possible.append(coin)

    return possible[0] if len(possible) == 1 else 0


def solve(data: str) -> str:
    """
    將題目輸入字串轉成輸出字串，並符合空白行格式。

    題目雖然有空白列分隔，但使用 split() 後可直接忽略空白行，
    因此只要依序讀取 token 即可。
    """
    tokens = data.split()
    idx = 0

    t = int(tokens[idx])
    idx += 1

    answers: list[str] = []

    for _ in range(t):
        # 每組資料：先讀硬幣數量 n 與秤重次數 k。
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        weighings: list[tuple[list[int], list[int], str]] = []
        for _ in range(k):
            # p 代表該次秤重每一邊各放幾顆硬幣。
            p = int(tokens[idx])
            idx += 1

            left = [int(x) for x in tokens[idx : idx + p]]
            idx += p
            right = [int(x) for x in tokens[idx : idx + p]]
            idx += p

            result = tokens[idx]
            idx += 1

            weighings.append((left, right, result))

        answers.append(str(_find_fake_coin(n, weighings)))

    # 題目要求不同測資答案之間要有一個空白列。
    return "\n\n".join(answers) + "\n"


def main() -> None:
    """標準輸入輸出入口（讀 stdin、寫 stdout）。"""
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

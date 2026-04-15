"""
UVA 948 假幣問題的單元測試程式。

說明：
1) 這份檔案先提供一個參考解 `reference_solve`，確保測試可獨立執行。
2) 若同資料夾有你的解答模組（例如 `solution_948.py`），
   且其中提供 `solve(data: str) -> str`，測試會自動改測你的函式。
"""

from __future__ import annotations

import importlib.util
import io
import os
import unittest
from pathlib import Path
from typing import Iterable


# -------------------------------
# 題目邏輯（參考解）
# -------------------------------
def _tokenize_input(data: str) -> list[str]:
    """把輸入切成 token；題目中的空白行會自動被忽略。"""
    return data.split()


def _result_from_diff(diff: int) -> str:
    """把左右重量差轉回題目符號。"""
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
    檢查某顆硬幣是否可能是假幣。

    sign = +1 代表它比較重，sign = -1 代表它比較輕。
    用「模擬秤重」驗證每次結果是否完全一致。
    """
    for left, right, expected in weighings:
        diff = 0
        if coin in left:
            diff += sign
        if coin in right:
            diff -= sign
        if _result_from_diff(diff) != expected:
            return False
    return True


def _find_fake_coin(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    """
    回傳可唯一確定的假幣編號；若不唯一（或無法判定）回傳 0。
    """
    possible_coins: set[int] = set()
    for coin in range(1, n + 1):
        if _is_coin_consistent(coin, +1, weighings) or _is_coin_consistent(
            coin, -1, weighings
        ):
            possible_coins.add(coin)

    return next(iter(possible_coins)) if len(possible_coins) == 1 else 0


def reference_solve(data: str) -> str:
    """依題目 I/O 格式解題，測資間輸出一個空白行。"""
    tokens = _tokenize_input(data)
    idx = 0

    m = int(tokens[idx])
    idx += 1

    answers: list[str] = []

    for _ in range(m):
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        weighings: list[tuple[list[int], list[int], str]] = []

        for _ in range(k):
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

    return "\n\n".join(answers) + "\n"


# -------------------------------
# 可選：自動載入學生解答
# -------------------------------
def _load_candidate_solve():
    """
    若存在 `solution_948.py` 且有 `solve(data)`，就用它來跑測試。
    否則 fallback 到參考解，確保測試檔可直接執行。
    """
    current_dir = Path(__file__).resolve().parent
    candidate = current_dir / "solution_948.py"

    if not candidate.exists():
        return reference_solve

    spec = importlib.util.spec_from_file_location("solution_948", candidate)
    if spec is None or spec.loader is None:
        return reference_solve

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    solve_fn = getattr(module, "solve", None)
    if callable(solve_fn):
        return solve_fn

    return reference_solve


SOLVE = _load_candidate_solve()


# -------------------------------
# 單元測試
# -------------------------------
class TestUVA948(unittest.TestCase):
    """針對 UVA 948 的核心情境設計測試。"""

    def test_unique_coin_from_single_weighing(self):
        """只有第 1 號硬幣符合秤重結果。"""
        data = """1

2 1
1 1 2
<
"""
        # 左邊較輕，若只有 1 號在左邊，則可唯一判定 1 號是假幣（較輕）。
        self.assertEqual(SOLVE(data), "1\n")

    def test_ambiguous_returns_zero(self):
        """資訊不足時必須輸出 0。"""
        data = """1

3 1
1 1 2
=
"""
        # 1 與 2 都是真幣，但 3 沒有出現在秤重中，無法判定其真偽。
        self.assertEqual(SOLVE(data), "0\n")

    def test_equal_then_imbalance_unique(self):
        """先用等重排除，再透過不平衡鎖定唯一假幣。"""
        data = """1

4 2
1 1 2
=
1 3 4
>
"""
        # 第一次得知 1、2 真；第二次左重右輕，唯一可能是 3 號較重。
        self.assertEqual(SOLVE(data), "3\n")

    def test_multiple_cases_with_blank_line_between_answers(self):
        """多組測資輸出格式：答案間必須有空白行。"""
        data = """2

2 1
1 1 2
<

3 1
1 1 2
=
"""
        self.assertEqual(SOLVE(data), "1\n\n0\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)

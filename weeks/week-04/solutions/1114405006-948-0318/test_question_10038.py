"""
UVA 10038（Jolly Jumpers）單元測試程式。

說明：
1. 檔內提供 `reference_solve`，確保測試可獨立執行。
2. 若同資料夾有 `solution_10038.py` 且提供 `solve(data: str) -> str`，
   測試會自動改測你的解答函式。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


def _is_jolly(seq: list[int]) -> bool:
    """判斷一個整數序列是否為 Jolly Jumper。"""
    n = len(seq)
    if n <= 1:
        return True

    diffs = set()
    for i in range(1, n):
        diffs.add(abs(seq[i] - seq[i - 1]))

    return diffs == set(range(1, n))


def reference_solve(data: str) -> str:
    """
    每行一組測資：第一個數是 n，後面 n 個數為序列。
    依序輸出 `Jolly` 或 `Not jolly`。
    """
    outputs: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1 : 1 + n]

        outputs.append("Jolly" if _is_jolly(seq) else "Not jolly")

    if not outputs:
        return ""

    return "\n".join(outputs) + "\n"


def _load_candidate_solve():
    """若存在 `solution_10038.py` 且有 solve 函式，則改用該解答測試。"""
    current_dir = Path(__file__).resolve().parent
    candidate = current_dir / "solution_10038.py"

    if not candidate.exists():
        return reference_solve

    spec = importlib.util.spec_from_file_location("solution_10038", candidate)
    if spec is None or spec.loader is None:
        return reference_solve

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    solve_fn = getattr(module, "solve", None)
    if callable(solve_fn):
        return solve_fn

    return reference_solve


SOLVE = _load_candidate_solve()


class TestQuestion10038(unittest.TestCase):
    """針對 Jolly Jumper 核心情境設計測試。"""

    def test_sample_like_cases(self):
        """常見範例型測資。"""
        data = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected = """Jolly
Not jolly
"""
        self.assertEqual(SOLVE(data), expected)

    def test_single_number_is_jolly(self):
        """長度為 1 的序列一定是 Jolly。"""
        data = """1 100
"""
        self.assertEqual(SOLVE(data), "Jolly\n")

    def test_duplicate_differences_not_jolly(self):
        """相鄰差值重複且缺值時，不是 Jolly。"""
        data = """4 1 1 1 1
"""
        self.assertEqual(SOLVE(data), "Not jolly\n")

    def test_multiple_lines_mixed(self):
        """多組測資混合情境。"""
        data = """6 1 4 2 3 7 6
4 3 6 8 11
1 7
"""
        expected = """Not jolly
Not jolly
Jolly
"""
        self.assertEqual(SOLVE(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

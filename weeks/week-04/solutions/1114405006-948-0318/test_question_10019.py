"""
UVA 10019（依目前題目檔描述）單元測試程式。

說明：
1. 本測試依 `QUESTION-10019.md` 內容設計：
   每行有兩個整數，輸出其差的絕對值。
2. 檔內提供 `reference_solve`，讓測試可獨立執行。
3. 若同資料夾存在 `solution_10019.py` 且提供 `solve(data: str) -> str`，
   測試會自動改測你的解答函式。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# -------------------------------
# 題目邏輯（參考解）
# -------------------------------
def reference_solve(data: str) -> str:
    """
    逐行讀取兩個整數，輸出絕對差值。

    題目沒有提供固定測資組數，因此採 EOF 模式：
    讀到檔案結尾為止。
    """
    out: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)

        out.append(str(abs(a - b)))

    if not out:
        return ""

    return "\n".join(out) + "\n"


# -------------------------------
# 可選：自動載入學生解答
# -------------------------------
def _load_candidate_solve():
    """
    若存在 `solution_10019.py` 且有 `solve(data)`，就改用該函式測試；
    否則使用參考解。
    """
    current_dir = Path(__file__).resolve().parent
    candidate = current_dir / "solution_10019.py"

    if not candidate.exists():
        return reference_solve

    spec = importlib.util.spec_from_file_location("solution_10019", candidate)
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
class TestQuestion10019(unittest.TestCase):
    """針對題目核心規則設計測試。"""

    def test_basic_pairs(self):
        """一般情況：多行資料各自輸出絕對差。"""
        data = """10 12
10 10
20 1
"""
        expected = """2
0
19
"""
        self.assertEqual(SOLVE(data), expected)

    def test_order_irrelevant(self):
        """題意允許任意順序，輸出都應為正差值。"""
        data = """100 3
3 100
"""
        expected = """97
97
"""
        self.assertEqual(SOLVE(data), expected)

    def test_large_numbers(self):
        """大數測試：確認仍能正確計算差值。"""
        data = """9223372036854775807 0
9223372036854775807 9223372036854775806
"""
        expected = """9223372036854775807
1
"""
        self.assertEqual(SOLVE(data), expected)

    def test_ignore_blank_lines(self):
        """空白行應被安全忽略。"""
        data = """

5 2

8 8

"""
        expected = """3
0
"""
        self.assertEqual(SOLVE(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
